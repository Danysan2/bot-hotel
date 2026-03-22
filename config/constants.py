# -*- coding: utf-8 -*-
"""Constantes del negocio - Hotel Merecure."""

# Información del hotel
HOTEL_NOMBRE = "Hotel Merecure"
HOTEL_SLOGAN = "Espacios cómodos, atención cercana y hospitalidad real."
HOTEL_TELEFONO = "+57 317 698 0346"
HOTEL_DIRECCION = "Calle 2 #2-32, Barrio El Progreso, Cravo Norte, Arauca"
HOTEL_SEDE = "Cravo Norte, Arauca"
HOTEL_HORARIO = "Lunes a domingo, 8:00 AM – 6:00 PM"

# Link de reservas en la página web — reemplaza con la URL real
HOTEL_WEB_RESERVAS = "https://www.hotelmerecure.com/reservas"

# Tipos de habitación
HABITACIONES = [
    {
        "id": "hab_sencilla",
        "nombre": "Sencilla",
        "descripcion": (
            "🛏️ *Habitación Sencilla*\n\n"
            "Ideal para viajeros solos o estadías de trabajo.\n\n"
            "✅ *Incluye:*\n"
            "• Una cama sencilla\n"
            "• Baño privado\n"
            "• Ventilador o aire acondicionado\n\n"
            "Escribe *volver* para ver otras habitaciones."
        ),
        # URL de la imagen — reemplaza con la URL real una vez subida al servidor
        "imagen_url": "",
        "imagen_caption": "Habitación Sencilla - Hotel Merecure",
    },
    {
        "id": "hab_doble",
        "nombre": "Doble",
        "descripcion": (
            "🛏️ *Habitación Doble*\n\n"
            "Perfecta para parejas, con cama doble y ambiente acogedor.\n\n"
            "✅ *Incluye:*\n"
            "• Una cama doble\n"
            "• Baño privado\n"
            "• Ventilador o aire acondicionado\n\n"
            "Escribe *volver* para ver otras habitaciones."
        ),
        # URL de la imagen — reemplaza con la URL real una vez subida al servidor
        "imagen_url": "",
        "imagen_caption": "Habitación Doble - Hotel Merecure",
    },
    {
        "id": "hab_familiar",
        "nombre": "Familiar",
        "descripcion": (
            "🛏️ *Habitación Familiar*\n\n"
            "Amplia y cómoda para toda la familia.\n\n"
            "✅ *Incluye:*\n"
            "• Una cama doble\n"
            "• Un camarote (dos camas sencillas)\n"
            "• Baño privado\n"
            "• Ventilador o aire acondicionado\n\n"
            "Escribe *volver* para ver otras habitaciones."
        ),
        # URL de la imagen — reemplaza con la URL real una vez subida al servidor
        "imagen_url": "",
        "imagen_caption": "Habitación Familiar - Hotel Merecure",
    },
]

# Información general del hotel
INFO_GENERAL = {
    "servicios": (
        "🏨 *Servicios - Hotel Merecure*\n\n"
        "✨ _Espacios cómodos, atención cercana y hospitalidad real._\n\n"
        "• 🍽️ Restaurante gourmet\n"
        "• 🛎️ Room service\n"
        "• 🛏️ Habitaciones sencilla, doble y familiar\n"
        "• 🚿 Baño privado en todas las habitaciones\n"
        "• 🌬️ Ventilador o aire acondicionado según preferencia\n\n"
        "📞 *+57 317 698 0346*\n"
        "🕐 Atención: Lunes a domingo, 8:00 AM – 6:00 PM\n\n"
        "Escribe *volver* para regresar al menú anterior."
    ),
    "restaurante": (
        "🍽️ *Restaurante Gourmet - Hotel Merecure*\n\n"
        "Disfruta de una experiencia culinaria única en el corazón de Cravo Norte.\n\n"
        "🕐 *Horario:*\n"
        "• 7:00 AM – 8:00 PM\n\n"
        "📞 *+57 317 698 0346*\n\n"
        "Escribe *volver* para regresar al menú anterior."
    ),
    "ubicacion": (
        "📍 *Ubicación - Hotel Merecure*\n\n"
        "📌 Calle 2 #2-32, Barrio El Progreso\n"
        "    Cravo Norte, Arauca, Colombia\n\n"
        "📞 *+57 317 698 0346*\n"
        "🕐 Atención: Lunes a domingo, 8:00 AM – 6:00 PM\n\n"
        "Escribe *volver* para regresar al menú anterior."
    ),
}

# Estados conversacionales
ESTADO_INICIO = "inicio"
ESTADO_MENU_PRINCIPAL = "menu_principal"
ESTADO_INFO_GENERAL = "info_general"
ESTADO_INFO_HABITACIONES = "info_habitaciones"
ESTADO_HANDOFF_HUMANO = "handoff_humano"

# Nombres de sheets
SHEET_CLIENTES = "clientes"
SHEET_SESIONES = "sesiones_chat"

# Comandos para reactivar el bot (solo el recepcionista/administrador puede usarlos)
COMANDOS_REACTIVAR_BOT = [
    "bot",
    "activar bot",
    "te dejo con el bot",
    "activate",
    "bot activo",
    "continua bot",
    "continúa bot",
    "vuelve bot",
    "bot on",
    "activar chatbot",
    "reactivar bot",
    "encender bot",
    "activar",
    "activa bot",
    "activa el bot",
    "enciende bot",
    "enciende el bot",
    "bot activado",
    "listo bot",
    "ya bot"
]

# Tiempo de reactivación automática del bot (en horas)
HORAS_REACTIVACION_AUTO = 12
