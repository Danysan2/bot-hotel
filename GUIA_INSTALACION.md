# 🚀 Guía de Instalación - Viajes Colombia Tours Chatbot

## 📋 Requisitos Previos

- Python 3.8 o superior
- Cuenta de Google Cloud con acceso a Sheets API
- Instancia de Evolution API configurada
- Número de WhatsApp Business

## 🔧 Instalación Paso a Paso

### 1. Clonar el Repositorio

```bash
git clone <tu-repositorio>
cd viajes-colombia-chatbot
```

### 2. Crear Entorno Virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar Google Sheets

1. Crear un proyecto en Google Cloud Console
2. Habilitar Google Sheets API
3. Crear credenciales de cuenta de servicio
4. Descargar el archivo JSON y guardarlo como `service_account.json`
5. Crear una hoja de cálculo en Google Sheets
6. Compartir la hoja con el email de la cuenta de servicio

#### Estructura de la Hoja de Cálculo

Crear las siguientes pestañas:

**Pestaña "clientes":**
```
ID | Teléfono | Nombre | Fecha Registro | Total Consultas | Última Consulta
```

**Pestaña "sesiones_chat":**
```
Teléfono | Estado | Datos Temp | Última Actualización
```

### 5. Configurar Evolution API

1. Obtener URL de tu instancia de Evolution API
2. Obtener API Key
3. Crear una instancia de WhatsApp
4. Configurar webhook apuntando a tu servidor

### 6. Variables de Entorno

Crear archivo `.env` en la raíz del proyecto:

```env
# Google Sheets
GOOGLE_SHEET_ID=tu_id_de_google_sheet

# Evolution API
EVOLUTION_API_URL=https://tu-instancia.evolution-api.com
EVOLUTION_API_KEY=tu_api_key_aqui
INSTANCE_NAME=nombre_de_tu_instancia

# Servidor
PORT=8000
HOST=0.0.0.0
```

### 7. Configurar Webhook

Ejecutar el script de configuración:

```bash
python configurar_webhook.py
```

### 8. Iniciar el Servidor

```bash
python start.py
```

El servidor estará disponible en `http://localhost:8000`

## 🧪 Probar el Sistema

### Probar Conexión con Google Sheets

```bash
python check_database.py
```

### Probar el Chatbot

```bash
python test_chatbot.py
```

### Probar Integración Completa

```bash
python test_integration.py
```

## 🐳 Despliegue con Docker

### Construir la Imagen

```bash
docker build -t viajes-colombia-chatbot .
```

### Ejecutar el Contenedor

```bash
docker-compose up -d
```

## 📱 Configurar WhatsApp

1. Escanear código QR desde Evolution API
2. Esperar conexión exitosa
3. Enviar mensaje de prueba al número configurado

## � Verificación

Envía "hola" al número de WhatsApp y deberías recibir el menú principal:

```
✈️ ¡Hola! Bienvenido a *Viajes Colombia Tours* 🇨🇴

Es un gusto tenerte aquí...
```

## 🛠️ Solución de Problemas

### Error de Conexión con Google Sheets

- Verificar que `service_account.json` existe
- Verificar que la hoja está compartida con la cuenta de servicio
- Verificar el GOOGLE_SHEET_ID en `.env`

### Error de Webhook

- Verificar que Evolution API está activa
- Verificar URL del webhook
- Verificar que el servidor está accesible públicamente

### El Bot No Responde

- Verificar logs del servidor
- Verificar estado de la instancia en Evolution API
- Verificar que el webhook está configurado correctamente

## 📞 Soporte

Para más ayuda, consulta la documentación completa o contacta al equipo de desarrollo.

## 🔄 Actualización

Para actualizar el sistema:

```bash
git pull origin main
pip install -r requirements.txt --upgrade
python start.py
```

## 🎯 Próximos Pasos

1. Personalizar destinos y hoteles en `config/constants.py`
2. Agregar imágenes de hoteles
3. Configurar promociones especiales
4. Personalizar mensajes del chatbot
5. Configurar notificaciones para asesores

¡Listo! Tu chatbot de Viajes Colombia Tours está funcionando. 🎉
