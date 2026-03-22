#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test para verificar que los mensajes incluyen la nota sobre contacto desde otro número."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from chatbot.engine import ChatbotEngine

def test_mensaje_otro_numero():
    """Prueba que todos los mensajes incluyan la nota sobre contacto desde otro número."""
    print("=" * 70)
    print("TEST: VERIFICAR NOTA DE CONTACTO DESDE OTRO NÚMERO")
    print("=" * 70)
    
    bot = ChatbotEngine()
    
    # Test 1: Boletos Nacionales
    print("\n" + "=" * 70)
    print("TEST 1: Boletos Nacionales")
    print("=" * 70)
    
    telefono1 = "573001111111"
    bot.procesar_mensaje(telefono1, "hola")
    bot.procesar_mensaje(telefono1, "1")  # Boletos nacionales
    respuesta = bot.procesar_mensaje(telefono1, "1")  # Tame
    
    print(respuesta)
    print("\n✓ Verificando contenido...")
    assert "Arauca → Tame" in respuesta
    assert "La asesora te contactará desde otro número de WhatsApp" in respuesta
    print("✅ Mensaje incluye nota sobre otro número")
    
    # Test 2: Boletos Internacionales
    print("\n" + "=" * 70)
    print("TEST 2: Boletos Internacionales")
    print("=" * 70)
    
    telefono2 = "573002222222"
    bot.procesar_mensaje(telefono2, "hola")
    bot.procesar_mensaje(telefono2, "2")  # Boletos internacionales
    respuesta = bot.procesar_mensaje(telefono2, "1")  # Ecuador
    
    print(respuesta)
    print("\n✓ Verificando contenido...")
    assert "Ecuador" in respuesta
    assert "La asesora te contactará desde otro número de WhatsApp" in respuesta
    print("✅ Mensaje incluye nota sobre otro número")
    
    # Test 3: Boletos Aéreos
    print("\n" + "=" * 70)
    print("TEST 3: Boletos Aéreos")
    print("=" * 70)
    
    telefono3 = "573003333333"
    bot.procesar_mensaje(telefono3, "hola")
    respuesta = bot.procesar_mensaje(telefono3, "3")  # Boletos aéreos
    
    print(respuesta)
    print("\n✓ Verificando contenido...")
    assert "Boletos Aéreos" in respuesta
    assert "La asesora te contactará desde otro número de WhatsApp" in respuesta
    print("✅ Mensaje incluye nota sobre otro número")
    
    # Test 4: Paquetes Turísticos
    print("\n" + "=" * 70)
    print("TEST 4: Paquetes Turísticos")
    print("=" * 70)
    
    telefono4 = "573004444444"
    bot.procesar_mensaje(telefono4, "hola")
    respuesta = bot.procesar_mensaje(telefono4, "4")  # Paquetes turísticos
    
    print(respuesta)
    print("\n✓ Verificando contenido...")
    assert "Paquetes Turísticos" in respuesta
    assert "La asesora te contactará desde otro número de WhatsApp" in respuesta
    print("✅ Mensaje incluye nota sobre otro número")
    
    # Resumen
    print("\n" + "=" * 70)
    print("RESUMEN")
    print("=" * 70)
    print("✅ Boletos Nacionales: Incluye nota ✓")
    print("✅ Boletos Internacionales: Incluye nota ✓")
    print("✅ Boletos Aéreos: Incluye nota ✓")
    print("✅ Paquetes Turísticos: Incluye nota ✓")
    print("\n📞 Todos los mensajes informan al cliente que:")
    print("   'La asesora te contactará desde otro número de WhatsApp'")
    print("\n🎉 TODOS LOS TESTS PASARON")
    print("=" * 70)

if __name__ == "__main__":
    try:
        test_mensaje_otro_numero()
    except AssertionError as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
    except Exception as e:
        print(f"\n❌ ERROR INESPERADO: {e}")
        import traceback
        traceback.print_exc()
