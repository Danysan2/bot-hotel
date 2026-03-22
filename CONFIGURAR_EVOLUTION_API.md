# 🚀 Guía Rápida: Configurar Evolution API

## 📋 Resumen del Problema

Los mensajes NO se envían porque el archivo `.env` tiene valores de ejemplo en lugar de tus credenciales reales de Evolution API.

## ✅ Solución en 3 Pasos

### Paso 1: Obtener Credenciales

Accede a tu panel de Evolution API y obtén:

1. **URL del servidor** (ejemplo: `https://api.evolution.com`)
2. **API Key** (ejemplo: `B6D711FCDE4D4FD5936544120E713976`)
3. **Nombre de instancia** (ejemplo: `mi_whatsapp`)

### Paso 2: Editar el Archivo .env

Abre el archivo `.env` y reemplaza estas líneas:

```env
# ANTES (valores de ejemplo - NO FUNCIONA):
EVOLUTION_API_URL=https://tu-instancia.evolution-api.com
EVOLUTION_API_KEY=tu_api_key_aqui
EVOLUTION_INSTANCE_NAME=nombre_de_tu_instancia

# DESPUÉS (tus valores reales):
EVOLUTION_API_URL=https://TU_URL_REAL
EVOLUTION_API_KEY=TU_API_KEY_REAL
EVOLUTION_INSTANCE_NAME=TU_INSTANCIA_REAL
```

El número profesional ya está configurado correctamente:
```env
PROFESSIONAL_PHONE=573001833654
```

### Paso 3: Probar la Configuración

Ejecuta el script de prueba:

```bash
python test_evolution_connection.py
```

Si todo está bien, verás:
```
✅ Todas las variables están configuradas
✅ Cliente creado exitosamente
✅ Estado obtenido: {...}
✅ ¡MENSAJE ENVIADO EXITOSAMENTE!
```

Y recibirás un mensaje de prueba en el WhatsApp **573001833654**.

## 🔄 Reiniciar el Servidor

Después de configurar, reinicia el servidor:

```bash
# Detener (Ctrl+C)
# Iniciar de nuevo:
python server.py
```

## 🧪 Probar el Sistema Completo

1. Envía un mensaje al chatbot desde otro número
2. Selecciona opción **3** (Boletos aéreos) o **4** (Paquetes turísticos)
3. El número **573001833654** debe recibir una notificación

## 📞 ¿No Tienes Evolution API?

Si no tienes Evolution API configurado, necesitas:

1. **Instalar Evolution API** en un servidor (VPS, cloud, etc.)
2. **Crear una instancia** de WhatsApp
3. **Conectar tu número** escaneando el código QR
4. **Obtener las credenciales** del panel

Documentación oficial: https://doc.evolution-api.com/

## 🆘 Ayuda Adicional

Si necesitas ayuda, revisa:
- `SOLUCION_ENVIO_MENSAJES.md` - Guía detallada completa
- Logs del servidor cuando envíes mensajes
- Estado de tu instancia en el panel de Evolution API
