"""
Test de envío de plantillas del Hotel Merecure por WhatsApp.
Ejecutar desde la carpeta chatbot/:  python test_plantillas.py
"""
import sys
import os
import time

sys.path.insert(0, os.path.dirname(__file__))

from dotenv import load_dotenv
load_dotenv()

from config.settings import EVOLUTION_API_URL, EVOLUTION_API_KEY, EVOLUTION_INSTANCE_NAME, PROFESSIONAL_PHONE
from services.evolution_api import EvolutionAPI
from config.constants import HABITACIONES, INFO_GENERAL

# ─────────────────────────────────────────
# Número destino del test (tu número en .env)
# ─────────────────────────────────────────
NUMERO_TEST = PROFESSIONAL_PHONE

api = EvolutionAPI()

# ──────────────────────────────────────────
# Verificar configuración antes de enviar
# ──────────────────────────────────────────
print("\n══════════════════════════════════════")
print("  TEST PLANTILLAS — Hotel Merecure")
print("══════════════════════════════════════")
print(f"  URL Evolution API : {EVOLUTION_API_URL or '❌ NO CONFIGURADA'}")
print(f"  Instancia         : {EVOLUTION_INSTANCE_NAME or '❌ NO CONFIGURADA'}")
print(f"  API Key           : {'✅ OK' if EVOLUTION_API_KEY else '❌ NO CONFIGURADA'}")
print(f"  Número destino    : {NUMERO_TEST}")
print("══════════════════════════════════════\n")

if not EVOLUTION_API_URL or not EVOLUTION_API_KEY or not EVOLUTION_INSTANCE_NAME:
    print("❌ Faltan variables de Evolution API en el .env. Abortando.")
    sys.exit(1)

ESPERA = 2  # segundos entre mensajes

def enviar(titulo: str, mensaje: str):
    print(f"📤 Enviando: {titulo}...")
    ok = api.send_message(NUMERO_TEST, mensaje)
    if ok:
        print(f"   ✅ OK\n")
    else:
        print(f"   ❌ Falló\n")
    time.sleep(ESPERA)
    return ok


# ─────────────────────────────────────────
# 1. Menú principal
# ─────────────────────────────────────────
enviar("Menú principal", (
    "🏨 ¡Hola! Bienvenido a *Hotel Merecure* 🌿\n"
    "✨ _Espacios cómodos, atención cercana y hospitalidad real._\n\n"
    "¿En qué podemos ayudarte?\n\n"
    "1️⃣ Reservar\n"
    "2️⃣ Reagendar una reserva\n"
    "3️⃣ Cancelar una reserva\n"
    "4️⃣ Habitaciones\n"
    "5️⃣ Información general\n\n"
    "Responde con el número de la opción."
))

# ─────────────────────────────────────────
# 2. Menú de habitaciones
# ─────────────────────────────────────────
enviar("Sub-menú habitaciones", (
    "🛏️ *Nuestras Habitaciones*\n\n"
    "¿Qué tipo de habitación te interesa?\n\n"
    "1️⃣ Sencilla\n"
    "2️⃣ Doble\n"
    "3️⃣ Familiar\n\n"
    "Escribe *volver* para regresar al menú principal."
))

# ─────────────────────────────────────────
# 3. Descripción de cada habitación
# ─────────────────────────────────────────
for hab in HABITACIONES:
    enviar(f"Habitación {hab['nombre']}", hab["descripcion"])

# ─────────────────────────────────────────
# 4. Menú información general
# ─────────────────────────────────────────
enviar("Sub-menú información general", (
    "ℹ️ *Información General - Hotel Merecure*\n\n"
    "¿Qué deseas conocer?\n\n"
    "1️⃣ Servicios\n"
    "2️⃣ Restaurante\n"
    "3️⃣ Ubicación\n\n"
    "Escribe *volver* para regresar al menú principal."
))

# ─────────────────────────────────────────
# 5. Secciones de información general
# ─────────────────────────────────────────
enviar("Servicios", INFO_GENERAL["servicios"])
enviar("Restaurante", INFO_GENERAL["restaurante"])
enviar("Ubicación", INFO_GENERAL["ubicacion"])

# ─────────────────────────────────────────
# 6. Mensaje de handoff (reserva/cancelar)
# ─────────────────────────────────────────
enviar("Handoff — Reserva", (
    "✅ *Solicitud recibida — Reserva*\n\n"
    "Un miembro de nuestro equipo te contactará en breve para ayudarte.\n\n"
    "⏰ Tiempo de respuesta: 5-10 minutos\n\n"
    "📞 También puedes llamarnos directamente:\n"
    "+57 317 698 0346\n\n"
    "_Un asesor humano te atenderá personalmente._"
))

print("══════════════════════════════════════")
print("  Test completado")
print("══════════════════════════════════════\n")
