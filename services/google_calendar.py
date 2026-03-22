"""Cliente para Google Calendar API."""
# ARCHIVO COMPLETAMENTE COMENTADO - No necesario para agencia de viajes
# La agencia de viajes solo proporciona información, no agenda citas

"""
import json
from datetime import datetime, date, time, timedelta
from typing import List, Optional, Dict, Any
import pytz
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

try:
    from loguru import logger
except ImportError:
    class SimpleLogger:
        def info(self, msg): print(f"INFO: {msg}")
        def error(self, msg): print(f"ERROR: {msg}")
    logger = SimpleLogger()

from config.settings import (
    SERVICE_ACCOUNT_PATH, GOOGLE_CALENDAR_ID,
    GOOGLE_SCOPES, TIMEZONE
)


class CalendarClient:
    # Cliente para interactuar con Google Calendar.
    # NO NECESARIO PARA AGENCIA DE VIAJES
    pass
"""

# Clase vacía para mantener compatibilidad
class CalendarClient:
    """Cliente deshabilitado - No necesario para agencia de viajes."""
    
    def __init__(self):
        """Inicializa cliente vacío."""
        pass
    
    def crear_evento(self, *args, **kwargs):
        """Método deshabilitado."""
        return None
    
    def eliminar_evento(self, *args, **kwargs):
        """Método deshabilitado."""
        return True
    
    def get_eventos_dia(self, *args, **kwargs):
        """Método deshabilitado."""
        return []
