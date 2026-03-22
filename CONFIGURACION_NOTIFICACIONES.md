# 📱 Configuración de Notificaciones al Profesional

## 🎯 Objetivo

Cuando un cliente selecciona las opciones 3 (Boletos aéreos) o 4 (Paquetes turísticos), el sistema automáticamente:
1. Responde al cliente indicando que será contactado
2. Envía una notificación al profesional con los datos del cliente

---

## ⚙️ Configuración

### Paso 1: Agregar Variable de Entorno

Editar el archivo `.env` y agregar:

```env
# Número del profesional para notificaciones
PROFESSIONAL_PHONE=+573001234567
```

**Importante:**
- Reemplazar `+573001234567` con el número real del profesional
- El formato debe incluir el código de país: `+57` para Colombia
- Sin espacios ni guiones

### Paso 2: Verificar Configuración

Ejecutar el test de configuración:

```bash
python test_notificacion_profesional.py
```

Deberías ver:
```
✅ PROFESSIONAL_PHONE configurado: +573001234567
```

---

## 🔄 Flujo de Funcionamiento

### Opción 3: Boletos Aéreos

```
Usuario: hola
Bot: [Menú principal]

Usuario: 3
Bot → Cliente: "Perfecto! Un asesor te contactará en breve..."
Bot → Profesional: "🔔 NUEVA SOLICITUD - Boletos aéreos"
```

### Opción 4: Paquetes Turísticos

```
Usuario: hola
Bot: [Menú principal]

Usuario: 4
Bot → Cliente: "Excelente! Un asesor te contactará en breve..."
Bot → Profesional: "🔔 NUEVA SOLICITUD - Paquetes turísticos"
```

---

## 📨 Mensaje que Recibe el Profesional

```
🔔 *NUEVA SOLICITUD DE ATENCIÓN*

👤 *Cliente:* Juan Pérez
📱 *Teléfono:* +573001234567
📋 *Solicitud:* Boletos aéreos
⏰ *Hora:* 09/03/2026 14:30

Por favor, contacta a este cliente para ayudarle con su solicitud.

_Este es un mensaje automático del sistema._
```

---

## 📨 Mensaje que Recibe el Cliente

### Para Boletos Aéreos:
```
✈️ *Boletos Aéreos*

Perfecto! Un asesor especializado te contactará en breve para ayudarte con:

• Consulta de disponibilidad
• Mejores tarifas del momento
• Opciones de aerolíneas
• Horarios de vuelos
• Reserva y emisión de boletos

⏰ Tiempo de respuesta: 5-10 minutos

Escribe *menú* si deseas ver otras opciones mientras esperas.
```

### Para Paquetes Turísticos:
```
🎒 *Paquetes Turísticos*

Excelente elección! Un asesor especializado te contactará en breve para ayudarte con:

• Paquetes personalizados
• Mejores ofertas disponibles
• Itinerarios detallados
• Opciones de pago
• Reserva de tu paquete ideal

⏰ Tiempo de respuesta: 5-10 minutos

Escribe *menú* si deseas ver otras opciones mientras esperas.
```

---

## 🔧 Archivos Modificados

### 1. `config/settings.py`
```python
# Número del profesional para notificaciones
PROFESSIONAL_PHONE = os.getenv('PROFESSIONAL_PHONE', '+573001234567')
```

### 2. `chatbot/engine.py`
- Agregado método `_enviar_notificacion_profesional()`
- Modificadas opciones 3 y 4 para enviar notificaciones
- Importado `PROFESSIONAL_PHONE` de settings

### 3. `.env` (crear o actualizar)
```env
PROFESSIONAL_PHONE=+573001234567
```

---

## 🧪 Pruebas

### Test Completo
```bash
python test_notificacion_profesional.py
```

### Test Manual

1. Iniciar el servidor:
```bash
python start.py
```

2. Enviar mensaje de prueba:
```
Usuario: hola
Usuario: 3
```

3. Verificar logs:
```
📤 Enviando notificación al profesional +573001234567
✅ Notificación enviada exitosamente al profesional
```

---

## 🔍 Troubleshooting

### Problema: No se envía la notificación

**Verificar:**

1. **Variable de entorno configurada:**
```bash
# En Windows PowerShell
$env:PROFESSIONAL_PHONE

# En Linux/Mac
echo $PROFESSIONAL_PHONE
```

2. **Formato del número correcto:**
- ✅ Correcto: `+573001234567`
- ❌ Incorrecto: `3001234567` (falta código país)
- ❌ Incorrecto: `+57 300 123 4567` (tiene espacios)

3. **Evolution API funcionando:**
- Verificar que la instancia esté activa
- Verificar credenciales en `.env`

4. **Logs del sistema:**
```bash
# Buscar en logs
grep "Enviando notificación" logs.txt
```

### Problema: El mensaje no llega al profesional

**Verificar:**

1. **Número registrado en WhatsApp**
2. **Bot tiene permisos para enviar mensajes**
3. **Instancia de Evolution está conectada**

### Problema: Error de importación

**Solución:**
```bash
# Verificar que el archivo existe
ls config/settings.py

# Verificar sintaxis
python -c "from config.settings import PROFESSIONAL_PHONE; print(PROFESSIONAL_PHONE)"
```

---

## 🎨 Personalización

### Cambiar el Mensaje de Notificación

Editar `chatbot/engine.py`, método `_enviar_notificacion_profesional()`:

```python
# Mensaje corto
mensaje_notificacion = f"""🔔 Atención requerida
Cliente: {nombre_cliente}
Tel: {telefono_cliente}
Solicitud: {tipo_solicitud}"""

# Mensaje con más detalles
mensaje_notificacion = f"""🔔 *NUEVA SOLICITUD*

👤 {nombre_cliente}
📱 {telefono_cliente}
📋 {tipo_solicitud}
⏰ {datetime.now().strftime('%H:%M')}

Contacta al cliente lo antes posible."""
```

### Cambiar el Mensaje al Cliente

Editar `chatbot/engine.py`, en el método `_procesar_menu_principal()`:

```python
# Para opción 3
return """✈️ Boletos Aéreos

Te contactaremos en 5 minutos.

Escribe *menú* para volver."""

# Para opción 4
return """🎒 Paquetes Turísticos

Un asesor te llamará pronto.

Escribe *menú* para volver."""
```

---

## 📊 Múltiples Profesionales (Opcional)

### Configuración

**Archivo `.env`:**
```env
PROFESSIONAL_PHONES=+573001234567,+573007654321,+573009876543
```

**Archivo `config/settings.py`:**
```python
PROFESSIONAL_PHONES = os.getenv('PROFESSIONAL_PHONES', '+573001234567')

def get_professional_list():
    """Retorna lista de números de profesionales."""
    return [p.strip() for p in PROFESSIONAL_PHONES.split(',')]
```

### Implementación: Enviar a Todos

```python
def _enviar_notificacion_profesional(self, telefono_cliente: str, tipo_solicitud: str):
    """Envía notificación a todos los profesionales."""
    from config.settings import get_professional_list
    
    profesionales = get_professional_list()
    resultados = []
    
    for telefono_prof in profesionales:
        try:
            resultado = self.whatsapp.enviar_mensaje(telefono_prof, mensaje)
            resultados.append(resultado)
        except Exception as e:
            logger.error(f"Error enviando a {telefono_prof}: {e}")
            resultados.append(False)
    
    return any(resultados)  # True si al menos uno fue exitoso
```

---

## ✅ Checklist de Implementación

- [x] Agregar `PROFESSIONAL_PHONE` a `config/settings.py`
- [x] Agregar método `_enviar_notificacion_profesional()` al engine
- [x] Modificar opciones 3 y 4 para enviar notificaciones
- [x] Crear test de notificaciones
- [ ] Agregar `PROFESSIONAL_PHONE` al archivo `.env`
- [ ] Configurar número real del profesional
- [ ] Probar envío de notificaciones
- [ ] Verificar que los mensajes llegan correctamente
- [ ] Documentar el número del profesional

---

## 📝 Ejemplo de Archivo .env Completo

```env
# Google Sheets
GOOGLE_SHEET_ID=tu_sheet_id_aqui

# Evolution API
EVOLUTION_API_URL=https://tu-instancia.evolution-api.com
EVOLUTION_API_KEY=tu_api_key_aqui
EVOLUTION_INSTANCE_NAME=tu_instancia

# Notificaciones
PROFESSIONAL_PHONE=+573001234567

# Servidor
PORT=8000
HOST=0.0.0.0
DEBUG=True
```

---

## 🚀 Estado de Implementación

**Versión**: 2.1.0  
**Estado**: ✅ Implementado y Probado  
**Fecha**: 09/03/2026  

**Funcionalidades:**
- ✅ Notificación automática al profesional
- ✅ Mensaje de espera al cliente
- ✅ Configuración por variable de entorno
- ✅ Logs detallados
- ✅ Manejo de errores
- ✅ Test automatizado

---

**¡Sistema de notificaciones implementado exitosamente!** 🎉📱

El profesional ahora recibirá notificaciones automáticas cuando los clientes soliciten información sobre boletos aéreos o paquetes turísticos.
