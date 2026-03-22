"""Funciones de validación para el chatbot."""
import re


def validar_opcion_numerica(mensaje: str, max_opcion: int) -> bool:
    """
    Valida que el mensaje sea un número válido dentro del rango.
    
    Args:
        mensaje: Mensaje del usuario
        max_opcion: Número máximo de opciones válidas
    
    Returns:
        True si es válido, False en caso contrario
    """
    try:
        opcion = int(mensaje.strip())
        return 1 <= opcion <= max_opcion
    except ValueError:
        return False


def validar_comando_menu(mensaje: str) -> bool:
    """
    Valida si el mensaje es un comando para volver al menú.
    
    Args:
        mensaje: Mensaje del usuario
    
    Returns:
        True si es un comando de menú
    """
    comandos = ['menu', 'menú', 'inicio', 'hola', 'volver', 'start']
    return mensaje.strip().lower() in comandos


def validar_nombre(mensaje: str) -> bool:
    """
    Valida que el mensaje sea un nombre válido.
    
    Args:
        mensaje: Mensaje del usuario
    
    Returns:
        True si es un nombre válido
    """
    # Solo letras y espacios, mínimo 2 caracteres
    patron = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{2,50}$'
    return bool(re.match(patron, mensaje.strip()))
