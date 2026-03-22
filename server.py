"""Servidor FastAPI — Hotel Merecure Chatbot."""
import os
import sys
import time
from typing import Dict

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

# ── Logger ────────────────────────────────────────────────
try:
    from loguru import logger
    # Crear carpeta de logs si no existe
    os.makedirs("logs", exist_ok=True)
    logger.remove()
    logger.add(sys.stderr, level="DEBUG")
    logger.add("logs/hotel_{time}.log", rotation="1 day", retention="7 days", level="INFO")
except ImportError:
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("hotel")

# ── Config ────────────────────────────────────────────────
from dotenv import load_dotenv
load_dotenv()

from config.settings import HOST, PORT, DEBUG

# ── Chatbot ───────────────────────────────────────────────
from chatbot import ChatbotEngine
from services.evolution_api import EvolutionAPI

chatbot = ChatbotEngine()
evolution = EvolutionAPI()

# ── App ───────────────────────────────────────────────────
app = FastAPI(
    title="Hotel Merecure Chatbot",
    description="Asistente virtual Hotel Merecure — Cravo Norte, Arauca",
    version="1.0.0"
)

# Cache anti-duplicados (5 segundos)
mensaje_cache: Dict[str, float] = {}
CACHE_TIMEOUT = 5


# ── Endpoints ─────────────────────────────────────────────

@app.get("/")
async def root():
    return {
        "status": "online",
        "service": "Hotel Merecure Chatbot",
        "version": "1.0.0"
    }


@app.get("/health")
async def health():
    estado_evolution = "unknown"
    try:
        info = evolution.get_instance_status()
        estado_evolution = "connected" if info else "error"
    except Exception as e:
        estado_evolution = f"error: {e}"

    return {
        "status": "healthy",
        "evolution_api": estado_evolution
    }


@app.post("/webhook")
async def webhook(request: Request):
    """Recibe mensajes de WhatsApp vía Evolution API."""
    try:
        data = await request.json()
        logger.debug(f"📨 Webhook recibido: {data}")
        return await _procesar_webhook(data)
    except Exception as e:
        logger.error(f"❌ Error en webhook: {e}")
        return JSONResponse({"status": "error", "message": str(e)})


@app.post("/")
async def webhook_raiz(request: Request):
    """Webhook alternativo en /  (por si Evolution API apunta aquí)."""
    try:
        data = await request.json()
        logger.debug(f"📨 Webhook en /: {data}")
        return await _procesar_webhook(data)
    except Exception as e:
        logger.error(f"❌ Error en webhook /: {e}")
        return JSONResponse({"status": "error", "message": str(e)})


# ── Lógica interna ─────────────────────────────────────────

async def _procesar_webhook(data: dict) -> dict:
    event_type = data.get("event")

    if event_type != "messages.upsert":
        return {"status": "ok", "skipped": event_type}

    message_data = data.get("data", {})
    key = message_data.get("key", {})
    message = message_data.get("message", {})

    # Ignorar mensajes propios
    if key.get("fromMe"):
        return {"status": "ok", "skipped": "fromMe"}

    telefono = key.get("remoteJid", "").replace("@s.whatsapp.net", "")

    texto = ""
    if "conversation" in message:
        texto = message["conversation"]
    elif "extendedTextMessage" in message:
        texto = message["extendedTextMessage"].get("text", "")

    if not telefono or not texto:
        return {"status": "ok", "skipped": "sin_texto"}

    # Anti-duplicados
    message_id = key.get("id", "")
    cache_key = f"{telefono}:{message_id}"
    now = time.time()

    if cache_key in mensaje_cache and now - mensaje_cache[cache_key] < CACHE_TIMEOUT:
        logger.info(f"⏭️  Duplicado ignorado: {telefono}")
        return {"status": "ok", "skipped": "duplicado"}

    mensaje_cache[cache_key] = now
    # Limpiar cache viejo
    viejos = [k for k, v in mensaje_cache.items() if now - v > CACHE_TIMEOUT]
    for k in viejos:
        mensaje_cache.pop(k, None)

    logger.info(f"💬 [{telefono}] → {texto}")

    # Procesar y responder
    try:
        respuesta = chatbot.procesar_mensaje(telefono, texto)

        if respuesta:
            ok = evolution.send_message(telefono, respuesta)
            if ok:
                logger.info(f"✅ Respuesta enviada a {telefono}")
            else:
                logger.error(f"❌ Fallo al enviar respuesta a {telefono}")
        else:
            logger.info(f"🔇 Sin respuesta para {telefono} (bot desactivado o None)")

    except Exception as e:
        logger.error(f"❌ Error procesando mensaje de {telefono}: {e}")
        import traceback
        logger.error(traceback.format_exc())

    return {"status": "ok"}


# ── Arranque ──────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn

    print(f"""
╔══════════════════════════════════════════════════╗
║        🏨  HOTEL MERECURE — CHATBOT              ║
║        📍  Cravo Norte, Arauca                   ║
╚══════════════════════════════════════════════════╝

  🌐  http://{HOST}:{PORT}
  📡  Webhook: http://{HOST}:{PORT}/webhook
  🔧  Health:  http://{HOST}:{PORT}/health

  Presiona CTRL+C para detener
""")

    uvicorn.run("server:app", host=HOST, port=PORT, reload=DEBUG)
