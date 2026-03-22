"""Configuración del sistema desde variables de entorno."""
import os
from dotenv import load_dotenv

load_dotenv()

# Evolution API
EVOLUTION_API_URL = os.getenv('EVOLUTION_API_URL', '')
EVOLUTION_API_KEY = os.getenv('EVOLUTION_API_KEY', '')
EVOLUTION_INSTANCE_NAME = os.getenv('EVOLUTION_INSTANCE_NAME', '')

# Número del recepcionista para notificaciones
PROFESSIONAL_PHONE = os.getenv('PROFESSIONAL_PHONE', '')

# Servidor
HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', 8002))
DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
