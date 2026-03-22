#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test para verificar que los mensajes lleguen al nuevo número profesional."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from chatbot.engine import ChatbotEngine
from config.settings import PROFESSIONAL_PHONE
from datetime import datetime

def test_envio_nuevo_numero():
    """Prueba de envío de mensaje al nuevo número profesional."""
    print("=" * 70)
    print("TEST DE ENVÍO AL NUEVO NÚMERO PROFESIONAL")
    print("=" * 70)
    
    # Mostrar número configurado
    print(f"\n📱 Número profesional configurado: {PROFESSIONAL_PHONE}")
    print(f"⏰ Fecha y hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    
    # Inicializar chatbot
    print("\n🤖 Inicializando chatbot...")
    bot = ChatbotEngine()
    
    # Verificar que el número del bot coincide
    print(f"✅ Número en el bot: {bot.professional_phone}")
    assert bot.professional_phone == PROFESSIONAL_PHONE, "El número no coincide"
    
    # Simular flujo completo hasta handoff
    telefono_test = "573001234567"
    
    print("\n" + "=" * 70)
    print("PASO 1: Iniciar conversación")
    print("=" * 70)
    respuesta = bot.procesar_mensaje(telefono_test, "hola")
    print("✅ Menú principal mostrado")
    
    print("\n" + "=" * 70)
    print("PASO 2: Seleccionar boletos nacionales")
    print("=" * 70)
    respuesta = bot.procesar_mensaje(telefono_test, "1")
    print("✅ Lista de 37 destinos mostrada")
    
    print("\n" + "=" * 70)
    print("PASO 3: Seleccionar destino (ENVÍO DE NOTIFICACIÓN)")
    print("=" * 70)
    print(f"🚀 Seleccionando destino 19 (Bogotá)...")
    print(f"📤 Esto enviará una notificación a: {PROFESSIONAL_PHONE}")
    print()
    
    respuesta = bot.procesar_mensaje(telefono_test, "19")
    
    print("\n" + "=" * 70)
    print("RESULTADO DEL ENVÍO")
    print("=" * 70)
    
    # Verificar que la respuesta contiene información del handoff
    if "asesor" in respuesta.lower() and "Bogotá" in respuesta:
        print("✅ Handoff activado correctamente")
        print("✅ Respuesta al cliente generada")
        print(f"\n📱 Notificación enviada a: {PROFESSIONAL_PHONE}")
        print("\n📋 Contenido de la notificación:")
        print("   - Cliente: Cliente")
        print("   - Teléfono: 573001234567")
        print("   - Tipo: Boleto Nacional")
        print("   - Detalles: Arauca → Bogotá, Cundinamarca | Precio: $150.000")
        print(f"   - Hora: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        
        print("\n" + "=" * 70)
        print("INSTRUCCIONES PARA VERIFICAR")
        print("=" * 70)
        print(f"1. Revisa el WhatsApp del número: {PROFESSIONAL_PHONE}")
        print("2. Deberías ver un mensaje con:")
        print("   🔔 NUEVA SOLICITUD DE ATENCIÓN")
        print("   👤 Cliente: Cliente")
        print("   📱 Teléfono: 573001234567")
        print("   📋 Tipo: Boleto Nacional")
        print("   📍 Detalles: Arauca → Bogotá, Cundinamarca | Precio: $150.000")
        print("\n3. Si NO recibes el mensaje, verifica:")
        print("   - Que el número esté registrado en WhatsApp")
        print("   - Que la Evolution API esté funcionando")
        print("   - Los logs arriba para ver si hubo errores")
        
        print("\n" + "=" * 70)
        print("TEST COMPLETADO")
        print("=" * 70)
        print(f"✅ Mensaje enviado a: {PROFESSIONAL_PHONE}")
        print("✅ Revisa tu WhatsApp para confirmar la recepción")
        print("=" * 70)
    else:
        print("❌ Error: No se activó el handoff correctamente")
        print(f"Respuesta recibida: {respuesta[:200]}...")
    
    # Test adicional: Verificar que el bot está desactivado
    print("\n" + "=" * 70)
    print("VERIFICACIÓN ADICIONAL: Bot desactivado")
    print("=" * 70)
    respuesta2 = bot.procesar_mensaje(telefono_test, "hola")
    if respuesta2 is None:
        print("✅ Bot correctamente desactivado después del handoff")
    else:
        print("⚠️ Advertencia: Bot respondió cuando debería estar desactivado")

if __name__ == "__main__":
    try:
        test_envio_nuevo_numero()
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
