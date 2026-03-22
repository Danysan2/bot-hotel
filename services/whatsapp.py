"""Servicio de mensajería WhatsApp."""
from typing import Optional

# Logger opcional
try:
    from loguru import logger
except ImportError:
    class SimpleLogger:
        def info(self, msg): print(f"INFO: {msg}")
        def error(self, msg): print(f"ERROR: {msg}")
        def warning(self, msg): print(f"WARNING: {msg}")
    logger = SimpleLogger()

from .evolution_api import EvolutionAPI


class WhatsAppService:
    """Servicio para enviar mensajes por WhatsApp."""
    
    def __init__(self):
        """Inicializa el servicio de WhatsApp."""
        self.evolution = EvolutionAPI()
    
    def enviar_mensaje(self, telefono: str, mensaje: str) -> bool:
        """Envía un mensaje por WhatsApp."""
        return self.evolution.send_message(telefono, mensaje)

    def enviar_imagen(self, telefono: str, imagen_url: str, caption: str = "") -> bool:
        """Envía una imagen por WhatsApp."""
        return self.evolution.send_media(telefono, imagen_url, caption)

    def enviar_menu_principal(self, telefono: str) -> bool:
        """Envía el menú principal del Hotel Merecure."""
        mensaje = """
🏨 *Bienvenido a Hotel Merecure*
📍 Cravo Norte, Arauca

¿En qué podemos ayudarte?

1️⃣ Reservar
2️⃣ Reagendar una reserva
3️⃣ Cancelar una reserva
4️⃣ Habitaciones
5️⃣ Información general

Responde con el número de la opción.
        """.strip()
        return self.enviar_mensaje(telefono, mensaje)
    
