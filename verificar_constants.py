"""Verificar contenido de constants.py"""
import os

print("Working dir:", os.getcwd())
print("File exists:", os.path.exists('config/constants.py'))

with open('config/constants.py', 'r', encoding='utf-8') as f:
    content = f.read()
    
print("Ecuador in file:", 'ecuador' in content.lower())
print("Miami in file:", 'miami' in content.lower())

# Buscar la línea de DESTINOS_INTERNACIONALES
lines = content.split('\n')
for i, line in enumerate(lines):
    if 'DESTINOS_INTERNACIONALES' in line:
        print(f"\nLine {i}: {line}")
        for j in range(i+1, min(i+10, len(lines))):
            print(f"Line {j}: {lines[j]}")
        break

# Ahora importar
print("\n--- Importando módulo ---")
from config.constants import DESTINOS_INTERNACIONALES
print("Keys:", list(DESTINOS_INTERNACIONALES.keys()))
