"""Motor principal del chatbot - Hotel Merecure."""
from typing import Any, Optional
from datetime import datetime

try:
    from loguru import logger
except ImportError:
    class SimpleLogger:
        def info(self, msg): print(f"INFO: {msg}")
        def error(self, msg): print(f"ERROR: {msg}")
        def warning(self, msg): print(f"WARNING: {msg}")
    logger = SimpleLogger()

from services import WhatsAppService
from models import Sesion
from config.constants import (
    HOTEL_NOMBRE,
    HOTEL_TELEFONO,
    HOTEL_WEB_RESERVAS,
    HABITACIONES,
    INFO_GENERAL,
    ESTADO_INICIO,
    ESTADO_MENU_PRINCIPAL,
    ESTADO_INFO_GENERAL,
    ESTADO_INFO_HABITACIONES,
    ESTADO_HANDOFF_HUMANO,
    COMANDOS_REACTIVAR_BOT,
    HORAS_REACTIVACION_AUTO,
)
from config.settings import PROFESSIONAL_PHONE


class ChatbotEngine:
    """Motor del chatbot conversacional para Hotel Merecure."""

    def __init__(self):
        self.sheets: Any = None  # asignado en _init_sheets
        self._init_sheets()
        try:
            self.whatsapp = WhatsAppService()
        except Exception:
            self.whatsapp = None
        self.professional_phone = PROFESSIONAL_PHONE

    def _init_sheets(self):
        class MockSheets:
            def __init__(self):
                self.sesiones: dict = {}
                self.row_counter = 1

            def get_sesion(self, telefono):
                if telefono in self.sesiones:
                    logger.info(f"🔍 Sesión encontrada para {telefono}")
                    return self.sesiones[telefono], self.row_counter
                return None

            def crear_sesion(self, sesion):
                self.sesiones[sesion.telefono] = sesion
                self.row_counter += 1
                return self.row_counter

            def actualizar_sesion(self, sesion, row):
                self.sesiones[sesion.telefono] = sesion
                return True

            def eliminar_sesion(self, telefono):
                self.sesiones.pop(telefono, None)
                return True

            def get_cliente_por_telefono(self, telefono):
                return None

            def crear_cliente(self, telefono, nombre):
                return None

        self.sheets = MockSheets()

    # ──────────────────────────────────────────────────────────
    # Punto de entrada
    # ──────────────────────────────────────────────────────────

    def procesar_mensaje(self, telefono: str, mensaje: str) -> Optional[str]:
        mensaje = mensaje.strip()
        msg = mensaje.lower()

        sesion_data = self.sheets.get_sesion(telefono)
        if sesion_data is None:
            sesion = Sesion(telefono=telefono, estado=ESTADO_INICIO, bot_activo=True)
            row_index = self.sheets.crear_sesion(sesion)
        else:
            sesion, row_index = sesion_data

        # ── Bot desactivado ──────────────────────────────────
        if not sesion.bot_activo:
            if sesion.handoff_timestamp:
                from datetime import timedelta
                if datetime.now() - sesion.handoff_timestamp > timedelta(hours=HORAS_REACTIVACION_AUTO):
                    sesion.bot_activo = True
                    sesion.handoff_timestamp = None
                    sesion.estado = ESTADO_INICIO
                    self.sheets.actualizar_sesion(sesion, row_index)
                    return self._menu_principal()

            if any(cmd in msg for cmd in COMANDOS_REACTIVAR_BOT):
                sesion.bot_activo = True
                sesion.handoff_timestamp = None
                sesion.estado = ESTADO_INICIO
                self.sheets.actualizar_sesion(sesion, row_index)
                return "✅ *Bot reactivado*\n\n" + self._menu_principal()

            return None

        # ── Navegación global ────────────────────────────────
        if msg in ['menu', 'menú', 'inicio', 'hola']:
            self.sheets.eliminar_sesion(telefono)
            return self._menu_principal()

        if msg == 'volver':
            # Desde habitaciones → vuelve a info general
            if sesion.estado == ESTADO_INFO_HABITACIONES:
                sesion.estado = ESTADO_INFO_GENERAL
                self.sheets.actualizar_sesion(sesion, row_index)
                return self._menu_info_general()
            # Desde info general → vuelve al menú principal
            if sesion.estado == ESTADO_INFO_GENERAL:
                self.sheets.eliminar_sesion(telefono)
                return self._menu_principal()

        # ── Despacho por estado ──────────────────────────────
        logger.info(f"Estado: {sesion.estado} | Msg: {msg}")

        if sesion.estado in (ESTADO_INICIO, ESTADO_MENU_PRINCIPAL):
            return self._procesar_menu_principal(telefono, msg, sesion, row_index)

        if sesion.estado == ESTADO_INFO_GENERAL:
            return self._procesar_info_general(telefono, msg, sesion, row_index)

        if sesion.estado == ESTADO_INFO_HABITACIONES:
            return self._procesar_habitaciones(telefono, msg, sesion, row_index)

        # Estado desconocido → resetear
        logger.warning(f"Estado desconocido '{sesion.estado}' — reseteando")
        self.sheets.eliminar_sesion(telefono)
        return self._menu_principal()

    # ──────────────────────────────────────────────────────────
    # Menú principal (4 opciones)
    # ──────────────────────────────────────────────────────────

    def _menu_principal(self) -> str:
        return (
            "🏨 ¡Hola! Bienvenido a *Hotel Merecure* 🌿\n"
            "✨ _Espacios cómodos, atención cercana y hospitalidad real._\n\n"
            "¿En qué podemos ayudarte?\n\n"
            "1️⃣ Reservar\n"
            "2️⃣ Reagendar una reserva\n"
            "3️⃣ Cancelar una reserva\n"
            "4️⃣ Información general\n\n"
            "Responde con el número de la opción."
        )

    def _procesar_menu_principal(self, telefono, msg, sesion, row_index) -> str:
        if msg not in ['1', '2', '3', '4']:
            return (
                "Por favor responde con un número del *1 al 4*.\n\n"
                + self._menu_principal()
            )

        if msg == '1':
            return (
                "🌐 *Reserva en línea — Hotel Merecure*\n\n"
                "Puedes hacer tu reserva directamente desde nuestra página web:\n\n"
                f"👉 {HOTEL_WEB_RESERVAS}\n\n"
                "Si tienes dudas antes de reservar, escríbenos y con gusto te ayudamos.\n\n"
                "📞 *+57 317 698 0346*\n\n"
                "Escribe *menu* para volver al inicio."
            )

        if msg == '2':
            return self._iniciar_handoff(telefono, sesion, row_index, "Reagendar reserva")

        if msg == '3':
            return self._iniciar_handoff(telefono, sesion, row_index, "Cancelar reserva")

        if msg == '4':
            sesion.estado = ESTADO_INFO_GENERAL
            sesion.datos_temp = {}
            self.sheets.actualizar_sesion(sesion, row_index)
            return self._menu_info_general()

        return "Opción inválida."

    # ──────────────────────────────────────────────────────────
    # Información general (servicios / restaurante / habitaciones / ubicación)
    # ──────────────────────────────────────────────────────────

    def _menu_info_general(self) -> str:
        return (
            "ℹ️ *Información General — Hotel Merecure*\n\n"
            "¿Qué deseas conocer?\n\n"
            "1️⃣ Servicios\n"
            "2️⃣ Restaurante\n"
            "3️⃣ Habitaciones\n"
            "4️⃣ Ubicación\n\n"
            "Escribe *volver* para regresar al menú principal."
        )

    def _procesar_info_general(self, telefono, msg, sesion, row_index) -> str:
        if msg == 'volver':
            self.sheets.eliminar_sesion(telefono)
            return self._menu_principal()

        if msg == '1':
            return INFO_GENERAL["servicios"]

        if msg == '2':
            return INFO_GENERAL["restaurante"]

        if msg == '3':
            sesion.estado = ESTADO_INFO_HABITACIONES
            self.sheets.actualizar_sesion(sesion, row_index)
            return self._menu_habitaciones()

        if msg == '4':
            return INFO_GENERAL["ubicacion"]

        return (
            "Opción inválida. Responde con un número del *1 al 4* o escribe *volver*.\n\n"
            + self._menu_info_general()
        )

    # ──────────────────────────────────────────────────────────
    # Habitaciones (dentro de información general)
    # ──────────────────────────────────────────────────────────

    def _menu_habitaciones(self) -> str:
        return (
            "🛏️ *Nuestras Habitaciones — Hotel Merecure*\n\n"
            "¿Cuál te gustaría conocer?\n\n"
            "1️⃣ Sencilla\n"
            "2️⃣ Doble\n"
            "3️⃣ Familiar\n\n"
            "Escribe *volver* para regresar al menú anterior."
        )

    def _procesar_habitaciones(self, telefono, msg, sesion, row_index) -> Optional[str]:
        if msg == 'volver':
            sesion.estado = ESTADO_INFO_GENERAL
            self.sheets.actualizar_sesion(sesion, row_index)
            return self._menu_info_general()

        if msg not in ['1', '2', '3']:
            return (
                "Opción inválida. Responde 1, 2 o 3, o escribe *volver*.\n\n"
                + self._menu_habitaciones()
            )

        hab = HABITACIONES[int(msg) - 1]

        # Enviar imagen si está configurada
        if hab["imagen_url"] and self.whatsapp:
            try:
                self.whatsapp.enviar_imagen(telefono, hab["imagen_url"], hab["imagen_caption"])
            except Exception as e:
                logger.warning(f"No se pudo enviar imagen: {e}")

        return hab["descripcion"]

    # ──────────────────────────────────────────────────────────
    # Handoff al recepcionista
    # ──────────────────────────────────────────────────────────

    def _iniciar_handoff(self, telefono, sesion, row_index, tipo: str) -> str:
        sesion.bot_activo = False
        sesion.handoff_timestamp = datetime.now()
        sesion.estado = ESTADO_HANDOFF_HUMANO
        sesion.datos_temp['tipo_solicitud'] = tipo
        self.sheets.actualizar_sesion(sesion, row_index)
        self._notificar_recepcionista(telefono, tipo)

        return (
            f"✅ *Solicitud recibida — {tipo}*\n\n"
            "Un miembro de nuestro equipo te contactará en breve.\n\n"
            "⏰ Tiempo de respuesta: 5-10 minutos\n\n"
            "📞 O llámanos directamente:\n"
            f"*{HOTEL_TELEFONO}*\n\n"
            "_Un asesor te atenderá personalmente._"
        )

    def _notificar_recepcionista(self, telefono_cliente: str, tipo: str) -> None:
        numero = telefono_cliente if telefono_cliente.startswith('+') else f'+{telefono_cliente}'
        msg = (
            f"🔔 *NUEVA SOLICITUD — {HOTEL_NOMBRE}*\n\n"
            f"📱 *Teléfono:* {numero}\n"
            f"📋 *Solicitud:* {tipo}\n"
            f"⏰ *Hora:* {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n"
            "Responde manualmente a este chat.\n\n"
            '_Para reactivar el bot escribe: "te dejo con el bot"_'
        )
        if self.whatsapp:
            try:
                self.whatsapp.enviar_mensaje(self.professional_phone, msg)
            except Exception as e:
                logger.error(f"Error notificando recepcionista: {e}")
        else:
            logger.info(f"[NOTIFICACIÓN]\n{msg}")
