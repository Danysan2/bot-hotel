"""Cliente para Evolution API."""
import requests
from typing import Optional, Dict, Any

# Logger opcional
try:
    from loguru import logger
except ImportError:
    class SimpleLogger:
        def info(self, msg): print(f"INFO: {msg}")
        def error(self, msg): print(f"ERROR: {msg}")
        def warning(self, msg): print(f"WARNING: {msg}")
    logger = SimpleLogger()

from config.settings import (
    EVOLUTION_API_URL, EVOLUTION_API_KEY, EVOLUTION_INSTANCE_NAME
)


class EvolutionAPI:
    """Cliente para interactuar con Evolution API."""
    
    def __init__(self):
        """Inicializa el cliente de Evolution API."""
        self.base_url = EVOLUTION_API_URL.rstrip('/')
        self.api_key = EVOLUTION_API_KEY
        self.instance_name = EVOLUTION_INSTANCE_NAME
        self.headers = {
            'apikey': self.api_key,
            'Content-Type': 'application/json'
        }
    
    def send_message(self, telefono: str, mensaje: str) -> bool:
        """Envía un mensaje de texto por WhatsApp."""
        url = f"{self.base_url}/message/sendText/{self.instance_name}"
        
        # Asegurar formato correcto del número (sin + al inicio)
        telefono_limpio = telefono.replace('+', '').strip()
        if not telefono_limpio.startswith('57'):
            telefono_limpio = f"57{telefono_limpio}"
        
        payload = {
            "number": telefono_limpio,
            "text": mensaje
        }
        
        # Logging detallado para debugging
        logger.info(f"📤 Intentando enviar mensaje a: {telefono_limpio}")
        logger.info(f"🔗 URL: {url}")
        logger.info(f"📋 Payload: {payload}")
        
        try:
            response = requests.post(url, json=payload, headers=self.headers, timeout=10)
            
            # Log de respuesta
            logger.info(f"📥 Status Code: {response.status_code}")
            logger.info(f"📥 Response: {response.text}")
            
            response.raise_for_status()
            logger.info(f"✅ Mensaje enviado exitosamente a {telefono_limpio}")
            return True
        except requests.exceptions.RequestException as e:
            logger.error(f"❌ Error enviando mensaje a {telefono_limpio}: {e}")
            if hasattr(e, 'response') and e.response is not None:
                logger.error(f"❌ Response body: {e.response.text}")
            return False
    
    def send_media(self, telefono: str, media_url: str, caption: str = "", file_name: str = "imagen.jpg") -> bool:
        """Envía una imagen por WhatsApp usando una URL pública."""
        url = f"{self.base_url}/message/sendMedia/{self.instance_name}"

        telefono_limpio = telefono.replace('+', '').strip()
        if not telefono_limpio.startswith('57'):
            telefono_limpio = f"57{telefono_limpio}"

        payload = {
            "number": telefono_limpio,
            "mediatype": "image",
            "mimetype": "image/jpeg",
            "caption": caption,
            "media": media_url,
            "fileName": file_name,
        }

        logger.info(f"📤 Enviando imagen a: {telefono_limpio}")
        logger.info(f"🔗 URL: {url}")

        try:
            response = requests.post(url, json=payload, headers=self.headers, timeout=15)
            logger.info(f"📥 Status Code: {response.status_code}")
            response.raise_for_status()
            logger.info(f"✅ Imagen enviada exitosamente a {telefono_limpio}")
            return True
        except requests.exceptions.RequestException as e:
            logger.error(f"❌ Error enviando imagen a {telefono_limpio}: {e}")
            if hasattr(e, 'response') and e.response is not None:
                logger.error(f"❌ Response body: {e.response.text}")
            return False

    def get_instance_status(self) -> Optional[Dict[str, Any]]:
        """Obtiene el estado de la instancia."""
        url = f"{self.base_url}/instance/connectionState/{self.instance_name}"
        
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error obteniendo estado de instancia: {e}")
            return None
    
    def get_qr_code(self) -> Optional[Dict[str, Any]]:
        """Obtiene el código QR para conectar WhatsApp."""
        url = f"{self.base_url}/instance/connect/{self.instance_name}"
        
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error obteniendo QR: {e}")
            return None
