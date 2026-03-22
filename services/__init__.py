from .google_sheets import SheetsClient
# CalendarClient comentado - no necesario para agencia de viajes
# from .google_calendar import CalendarClient
from .evolution_api import EvolutionAPI
from .whatsapp import WhatsAppService

# Importar CalendarClient vacío para compatibilidad
try:
    from .google_calendar import CalendarClient
except:
    class CalendarClient:
        def __init__(self): pass
        def crear_evento(self, *args, **kwargs): return None
        def eliminar_evento(self, *args, **kwargs): return True
        def get_eventos_dia(self, *args, **kwargs): return []

__all__ = ['SheetsClient', 'CalendarClient', 'EvolutionAPI', 'WhatsAppService']
