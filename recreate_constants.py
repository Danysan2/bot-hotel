#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script para recrear config/constants.py con precios."""

CONTENT = """# -*- coding: utf-8 -*-
\"\"\"Constantes del negocio.\"\"\"

# Información de la agencia
AGENCIA_NOMBRE = "Viajes Colombia Tours"
AGENCIA_TELEFONO = "+57 300 000 0000"
AGENCIA_SEDE = "Bogotá, Colombia"
AGENCIA_HORARIO = "Lunes a sábado, 8am – 6pm"

# Destinos nacionales desde Arauca con precios
DESTINOS_NACIONALES_DESDE_ARAUCA = [
    {"nombre": "Tame", "departamento": "Arauca", "precio": 60000},
    {"nombre": "Saravena", "departamento": "Arauca", "precio": 60000},
    {"nombre": "Paz de Ariporo", "departamento": "Casanare", "precio": 100000},
    {"nombre": "Yopal", "departamento": "Casanare", "precio": 110000},
    {"nombre": "Pore", "departamento": "Casanare", "precio": 110000},
    {"nombre": "La Chaparrera", "departamento": "Casanare", "precio": 110000},
    {"nombre": "Venado", "departamento": "Casanare", "precio": 120000},
    {"nombre": "Aguazul", "departamento": "Casanare", "precio": 120000},
    {"nombre": "Monterrey", "departamento": "Casanare", "precio": 130000},
    {"nombre": "Villanueva", "departamento": "Casanare", "precio": 130000},
    {"nombre": "Restrepo", "departamento": "Meta", "precio": 150000},
    {"nombre": "Cumaral", "departamento": "Meta", "precio": 150000},
    {"nombre": "Villavicencio", "departamento": "Meta", "precio": 150000},
    {"nombre": "Sogamoso", "departamento": "Boyacá", "precio": 150000},
    {"nombre": "Tunja", "departamento": "Boyacá", "precio": 150000},
    {"nombre": "Duitama", "departamento": "Boyacá", "precio": 150000},
    {"nombre": "Briceño", "departamento": "Boyacá", "precio": 150000},
    {"nombre": "Paipa", "departamento": "Boyacá", "precio": 150000},
    {"nombre": "Bogotá", "departamento": "Cundinamarca", "precio": 150000},
    {"nombre": "Cúcuta", "departamento": "Norte de Santander", "precio": 150000},
    {"nombre": "Bucaramanga", "departamento": "Santander", "precio": 150000},
    {"nombre": "Ibagué", "departamento": "Tolima", "precio": 230000},
    {"nombre": "Cali", "departamento": "Valle del Cauca", "precio": 270000},
    {"nombre": "Armenia", "departamento": "Quindío", "precio": 270000},
    {"nombre": "Pereira", "departamento": "Risaralda", "precio": 270000},
    {"nombre": "Tuluá", "departamento": "Valle del Cauca", "precio": 270000},
    {"nombre": "Neiva", "departamento": "Huila", "precio": 270000},
    {"nombre": "Manizales", "departamento": "Caldas", "precio": 270000},
    {"nombre": "Medellín", "departamento": "Antioquia", "precio": 290000},
    {"nombre": "Pitalito", "departamento": "Huila", "precio": 300000},
    {"nombre": "Pasto", "departamento": "Nariño", "precio": 360000},
    {"nombre": "Ipiales", "departamento": "Nariño", "precio": 360000}
]

# Destinos internacionales - Ecuador, Perú y Chile
DESTINOS_INTERNACIONALES = {
    "ecuador": {
        "id": "dest_ecuador",
        "nombre": "Ecuador",
        "emoji": "🇪🇨",
        "ciudades": ["Quito", "Guayaquil"]
    },
    "peru": {
        "id": "dest_peru",
        "nombre": "Perú",
        "emoji": "🇵🇪",
        "ciudades": ["Lima"]
    },
    "chile": {
        "id": "dest_chile",
        "nombre": "Chile",
        "emoji": "🇨🇱",
        "ciudades": ["Santiago de Chile"]
    }
}

# Boletos aéreos (rutas populares)
BOLETOS_AEREOS = {
    "nacionales": [
        {
            "id": "vuelo_bog_ctg",
            "ruta": "Bogotá → Cartagena",
            "aerolinea": "Avianca / LATAM",
            "precio_desde": 180000,
            "duracion": "1h 30min"
        },
        {
            "id": "vuelo_bog_med",
            "ruta": "Bogotá → Medellín",
            "aerolinea": "Avianca / LATAM",
            "precio_desde": 150000,
            "duracion": "1h"
        },
        {
            "id": "vuelo_bog_cali",
            "ruta": "Bogotá → Cali",
            "aerolinea": "Avianca / LATAM",
            "precio_desde": 160000,
            "duracion": "1h 15min"
        }
    ],
    "internacionales": [
        {
            "id": "vuelo_bog_mia",
            "ruta": "Bogotá → Miami",
            "aerolinea": "Avianca / Copa",
            "precio_desde": 850000,
            "duracion": "4h"
        },
        {
            "id": "vuelo_bog_can",
            "ruta": "Bogotá → Cancún",
            "aerolinea": "Avianca / Wingo",
            "precio_desde": 750000,
            "duracion": "3h 30min"
        },
        {
            "id": "vuelo_bog_mad",
            "ruta": "Bogotá → Madrid",
            "aerolinea": "Avianca / Iberia",
            "precio_desde": 1800000,
            "duracion": "10h"
        }
    ]
}

# Paquetes turísticos
PAQUETES_TURISTICOS = [
    {
        "id": "paq_cartagena_3d",
        "nombre": "Cartagena Mágica",
        "destino": "Cartagena",
        "duracion": "3 días / 2 noches",
        "precio": 899000,
        "incluye": [
            "Boletos aéreos ida y vuelta",
            "Hotel 4 estrellas con desayuno",
            "Traslados aeropuerto-hotel",
            "City tour por el centro histórico",
            "Seguro de viaje"
        ],
        "tipo": "nacional"
    },
    {
        "id": "paq_san_andres_5d",
        "nombre": "San Andrés Paraíso",
        "destino": "San Andrés",
        "duracion": "5 días / 4 noches",
        "precio": 1450000,
        "incluye": [
            "Boletos aéreos ida y vuelta",
            "Hotel frente al mar con desayuno",
            "Traslados aeropuerto-hotel",
            "Tour a Johnny Cay",
            "Snorkeling en el acuario",
            "Seguro de viaje"
        ],
        "tipo": "nacional"
    },
    {
        "id": "paq_eje_cafetero_4d",
        "nombre": "Eje Cafetero Experiencia",
        "destino": "Eje Cafetero",
        "duracion": "4 días / 3 noches",
        "precio": 1100000,
        "incluye": [
            "Boletos aéreos a Pereira",
            "Hotel campestre con desayuno",
            "Tour por fincas cafeteras",
            "Visita al Parque del Café",
            "Traslados incluidos",
            "Seguro de viaje"
        ],
        "tipo": "nacional"
    },
    {
        "id": "paq_cancun_5d",
        "nombre": "Cancún Todo Incluido",
        "destino": "Cancún, México",
        "duracion": "5 días / 4 noches",
        "precio": 2800000,
        "incluye": [
            "Boletos aéreos internacionales",
            "Hotel todo incluido 5 estrellas",
            "Traslados aeropuerto-hotel",
            "Tour a Chichén Itzá",
            "Seguro de viaje internacional"
        ],
        "tipo": "internacional"
    },
    {
        "id": "paq_miami_6d",
        "nombre": "Miami Shopping & Playa",
        "destino": "Miami, USA",
        "duracion": "6 días / 5 noches",
        "precio": 3200000,
        "incluye": [
            "Boletos aéreos internacionales",
            "Hotel en Miami Beach",
            "Traslados aeropuerto-hotel",
            "Tour por la ciudad",
            "Día libre para compras",
            "Seguro de viaje internacional"
        ],
        "tipo": "internacional"
    }
]

# Estados conversacionales
ESTADO_INICIO = "inicio"
ESTADO_MENU_PRINCIPAL = "menu_principal"
ESTADO_BOLETOS_NACIONALES = "boletos_nacionales"
ESTADO_BOLETOS_INTERNACIONALES = "boletos_internacionales"
ESTADO_BOLETOS_AEREOS = "boletos_aereos"
ESTADO_PAQUETES_TURISTICOS = "paquetes_turisticos"
ESTADO_VER_DETALLE_PAQUETE = "ver_detalle_paquete"

# Nombres de sheets (mantener compatibilidad)
SHEET_CLIENTES = "clientes"
SHEET_SESIONES = "sesiones_chat"

# Estado adicional para handoff
ESTADO_HANDOFF_HUMANO = "handoff_humano"  # Bot desactivado, humano atendiendo

# Comandos para reactivar el bot
COMANDOS_REACTIVAR_BOT = [
    "activar bot",
    "te dejo con el bot",
    "bot activo",
    "continua bot",
    "continúa bot",
    "vuelve bot",
    "bot on",
    "activar chatbot"
]

# Tiempo de reactivación automática del bot (en horas)
HORAS_REACTIVACION_AUTO = 12
"""

if __name__ == "__main__":
    with open('config/constants.py', 'w', encoding='utf-8') as f:
        f.write(CONTENT)
    print("✅ Archivo config/constants.py recreado exitosamente")
    print(f"   Tamaño: {len(CONTENT)} caracteres")
