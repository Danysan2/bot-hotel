"""Cliente para Google Sheets API - Versión simplificada para agencia de viajes."""
import uuid
import json
from datetime import datetime
from typing import Optional

# Importaciones opcionales
try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    GOOGLE_AVAILABLE = True
except ImportError:
    GOOGLE_AVAILABLE = False

# Logger opcional
try:
    from loguru import logger
except ImportError:
    class SimpleLogger:
        def info(self, msg): print(f"INFO: {msg}")
        def error(self, msg): print(f"ERROR: {msg}")
        def warning(self, msg): print(f"WARNING: {msg}")
    logger = SimpleLogger()

try:
    from config.settings import SERVICE_ACCOUNT_PATH, GOOGLE_SHEETS_ID, GOOGLE_SCOPES
    from config.constants import SHEET_CLIENTES, SHEET_SESIONES
    from models import Cliente, Sesion
except ImportError:
    logger.warning("⚠️  Configuración no disponible - modo mock")
    SHEET_CLIENTES = "clientes"
    SHEET_SESIONES = "sesiones_chat"


class SheetsClient:
    """Cliente simplificado - Solo usa memoria (sin Google Sheets)."""
    
    def __init__(self):
        """Inicializa el cliente en modo memoria."""
        # SIEMPRE usar diccionarios en memoria
        self._mock_sesiones = {}
        self._mock_clientes = {}
        self.service = None  # Desactivar Google Sheets completamente
        logger.info("✅ Sistema de sesiones en memoria activado")
    
    def _read_range(self, range_name: str):
        """Lee un rango."""
        if not self.service:
            return []
        try:
            result = self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range=range_name
            ).execute()
            return result.get('values', [])
        except:
            return []
    
    def _append_row(self, sheet_name: str, values):
        """Agrega una fila."""
        if not self.service:
            return True
        try:
            self.service.spreadsheets().values().append(
                spreadsheetId=self.spreadsheet_id,
                range=f"{sheet_name}!A:Z",
                valueInputOption='RAW',
                body={'values': [values]}
            ).execute()
            return True
        except:
            return False
    
    def _update_row(self, range_name: str, values):
        """Actualiza una fila."""
        if not self.service:
            return True
        try:
            self.service.spreadsheets().values().update(
                spreadsheetId=self.spreadsheet_id,
                range=range_name,
                valueInputOption='RAW',
                body={'values': [values]}
            ).execute()
            return True
        except:
            return False
    
    # === CLIENTES ===
    
    def get_cliente_por_telefono(self, telefono: str) -> Optional:
        """Busca un cliente por teléfono."""
        # Siempre usar memoria
        if telefono in self._mock_clientes:
            return self._mock_clientes[telefono]
        return None
    
    def crear_cliente(self, telefono: str, nombre: str):
        """Crea un nuevo cliente."""
        try:
            from models import Cliente
            cliente = Cliente(
                id=f"cli_{uuid.uuid4().hex[:8]}",
                telefono=telefono,
                nombre=nombre,
                fecha_registro=datetime.now(),
                total_citas=0
            )
            # Guardar en memoria
            self._mock_clientes[telefono] = cliente
            logger.info(f"✅ Cliente creado en memoria: {cliente.id}")
            return cliente
        except:
            return None
    
    def actualizar_cliente(self, cliente, row_index: int) -> bool:
        """Actualiza un cliente."""
        # Guardar en memoria
        self._mock_clientes[cliente.telefono] = cliente
        return True
    
    # === SESIONES ===
    
    def get_sesion(self, telefono: str):
        """Obtiene la sesión de un usuario."""
        # SIEMPRE usar memoria
        if telefono in self._mock_sesiones:
            sesion = self._mock_sesiones[telefono]
            logger.info(f"🔍 Sesión recuperada: {telefono} - Estado: {sesion.estado}")
            return sesion, 1
        logger.info(f"🔍 Sesión no encontrada: {telefono}")
        return None
    
    def crear_sesion(self, sesion) -> bool:
        """Crea una nueva sesión."""
        # SIEMPRE usar memoria
        self._mock_sesiones[sesion.telefono] = sesion
        logger.info(f"✅ Sesión creada: {sesion.telefono} - Estado: {sesion.estado}")
        return True
    
    def actualizar_sesion(self, sesion, row_index: int) -> bool:
        """Actualiza una sesión."""
        # SIEMPRE usar memoria
        sesion.ultima_actividad = datetime.now()
        self._mock_sesiones[sesion.telefono] = sesion
        logger.info(f"✏️ Sesión actualizada: {sesion.telefono} - Estado: {sesion.estado}")
        return True
    
    def eliminar_sesion(self, telefono: str) -> bool:
        """Elimina una sesión."""
        # SIEMPRE usar memoria
        if telefono in self._mock_sesiones:
            del self._mock_sesiones[telefono]
            logger.info(f"🗑️ Sesión eliminada: {telefono}")
        return True
    
    def test_connection(self) -> bool:
        """Prueba la conexión."""
        # Siempre retornar True ya que usamos memoria
        return True
