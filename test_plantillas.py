"""
Test de envío de plantillas del Hotel Merecure por WhatsApp.
Ejecutar desde la carpeta chatbot/:  python test_plantillas.py
"""
import sys
import os
import time

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
load_dotenv()

from config.settings import EVOLUTION_API_URL, EVOLUTION_API_KEY, EVOLUTION_INSTANCE_NAME, PROFESSIONAL_PHONE
from services.evolution_api import EvolutionAPI
from config.constants import HABITACIONES, INFO_GENERAL, HOTEL_WEB_RESERVAS

NUMERO_TEST = PROFESSIONAL_PHONE
api = EvolutionAPI()

print("\n══════════════════════════════════════════")
print("   TEST PLANTILLAS — Hotel Merecure")
print("══════════════════════════════════════════")
print(f"  URL  : {EVOLUTION_API_URL or '❌ NO CONFIGURADA'}")
print(f"  Inst : {EVOLUTION_INSTANCE_NAME or '❌ NO CONFIGURADA'}")
print(f"  Key  : {'✅ OK' if EVOLUTION_API_KEY else '❌ NO CONFIGURADA'}")
print(f"  Tel  : {NUMERO_TEST or '❌ NO CONFIGURADO'}")
print("══════════════════════════════════════════\n")

if not all([EVOLUTION_API_URL, EVOLUTION_API_KEY, EVOLUTION_INSTANCE_NAME, NUMERO_TEST]):
    print("❌ Faltan variables en el .env. Abortando.")
    sys.exit(1)

PAUSA = 2
resultados = {"ok": 0, "fail": 0}

def enviar(titulo: str, mensaje: str):
    print(f"📤 {titulo}...")
    ok = api.send_message(NUMERO_TEST, mensaje)
    if ok:
        print(f"   ✅ OK")
        resultados["ok"] += 1
    else:
        print(f"   ❌ Falló")
        resultados["fail"] += 1
    time.sleep(PAUSA)

# ── 1. Menú principal ─────────────────────────────────────
enviar("Menú principal", (
    "🏨 ¡Hola! Bienvenido a *Hotel Merecure* 🌿\n"
    "✨ _Espacios cómodos, atención cercana y hospitalidad real._\n\n"
    "¿En qué podemos ayudarte?\n\n"
    "1️⃣ Reservar\n"
    "2️⃣ Reagendar una reserva\n"
    "3️⃣ Cancelar una reserva\n"
    "4️⃣ Información general\n\n"
    "Responde con el número de la opción."
))

# ── 2. Opción 1 — Reservar ────────────────────────────────
enviar("Respuesta opción 1 — Reservar", (
    "🌐 *Reserva en línea — Hotel Merecure*\n\n"
    "Puedes hacer tu reserva directamente desde nuestra página web:\n\n"
    f"👉 {HOTEL_WEB_RESERVAS}\n\n"
    "Si tienes dudas antes de reservar, escríbenos y con gusto te ayudamos.\n\n"
    "📞 *+57 317 698 0346*\n\n"
    "Escribe *menu* para volver al inicio."
))

# ── 3. Opción 2/3 — Handoff ───────────────────────────────
enviar("Respuesta handoff — Reagendar/Cancelar", (
    "✅ *Solicitud recibida — Reagendar reserva*\n\n"
    "Un miembro de nuestro equipo te contactará en breve.\n\n"
    "⏰ Tiempo de respuesta: 5-10 minutos\n\n"
    "📞 O llámanos directamente:\n"
    "*+57 317 698 0346*\n\n"
    "_Un asesor te atenderá personalmente._"
))

# ── 4. Menú información general ───────────────────────────
enviar("Sub-menú Información general", (
    "ℹ️ *Información General — Hotel Merecure*\n\n"
    "¿Qué deseas conocer?\n\n"
    "1️⃣ Servicios\n"
    "2️⃣ Restaurante\n"
    "3️⃣ Habitaciones\n"
    "4️⃣ Ubicación\n\n"
    "Escribe *volver* para regresar al menú principal."
))

# ── 5. Servicios ──────────────────────────────────────────
enviar("Servicios", INFO_GENERAL["servicios"])

# ── 6. Restaurante ────────────────────────────────────────
enviar("Restaurante", INFO_GENERAL["restaurante"])

# ── 7. Sub-menú habitaciones ──────────────────────────────
enviar("Sub-menú Habitaciones", (
    "🛏️ *Nuestras Habitaciones — Hotel Merecure*\n\n"
    "¿Cuál te gustaría conocer?\n\n"
    "1️⃣ Sencilla\n"
    "2️⃣ Doble\n"
    "3️⃣ Familiar\n\n"
    "Escribe *volver* para regresar al menú anterior."
))

# ── 8. Descripción de cada habitación ────────────────────
for hab in HABITACIONES:
    enviar(f"Habitación {hab['nombre']}", hab["descripcion"])

# ── 9. Ubicación ─────────────────────────────────────────
enviar("Ubicación", INFO_GENERAL["ubicacion"])

# ── Resumen ───────────────────────────────────────────────
print(f"\n══════════════════════════════════════════")
print(f"  Resultado: {resultados['ok']} ✅  |  {resultados['fail']} ❌")
print(f"══════════════════════════════════════════\n")

if resultados["fail"] > 0:
    sys.exit(1)
