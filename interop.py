# PREGUNTAS REFLEXION
# 1
# Ambas permiten acceder a archivos entre Windows y Ubuntu, pero usando sistemas operativos diferentes.
# /mnt/c/ es usado en UBUNTU y \\wsl$\Ubuntu\ es usado en Windows.
#
# 2
# Ubuntu puede leer archivos NTFS porque WSL monta automaticamente las unidades de Windows al iniciar.
# Un punto de montaje (mount point) es una carpeta donde se conecta otro sistema de archivos para poder acceder a el.
# WSL monta la unidad C: en /mnt/c/, permitiendo que Ubuntu lea y modifique archivos en Windows como si fuera parte del mismo sistema.
# 
# 3
# Se puede relacionar con la arquitectura de sistemas operativos, porque WSL funciona como una capa de 
# compatibilidad entre Windows y Linux, lo que deja que interactuen y tengan sus archvos compartidos.


import os
import subprocess
from datetime import datetime

# ─────────────────────────────────────────────
# CONFIGURACIÓN — edita estas rutas
# ─────────────────────────────────────────────

USUARIO_WINDOWS = "cliente"
USUARIO_UBUNTU = "jia"

# Rutas
carpeta_windows = f"/mnt/c/Users/{USUARIO_WINDOWS}/Documents/practica_so"
carpeta_ubuntu = f"/home/{USUARIO_UBUNTU}/datos_ubuntu"

# ─────────────────────────────────────────────
# 1. Leer archivo que está en Windows
# ─────────────────────────────────────────────

ruta_origen = os.path.join(carpeta_windows, "reporte.txt")

print("\n📂 Leyendo desde Windows...")

with open(ruta_origen, 'r') as f:
    contenido = f.read()

print(contenido)

# ─────────────────────────────────────────────
# 2. Recolectar info adicional desde Ubuntu
# ─────────────────────────────────────────────

info_ubuntu = subprocess.run(
    ['bash', '-c', 'free -h | grep Mem'],
    capture_output=True,
    text=True
).stdout.strip()

# ─────────────────────────────────────────────
# 3. Guardar reporte combinado en Ubuntu
# ─────────────────────────────────────────────

ruta_destino = os.path.join(carpeta_ubuntu, "reporte_combinado.txt")

with open(ruta_destino, 'w') as f:
    f.write("=== REPORTE COMBINADO Windows + Ubuntu ===\n")
    f.write(f"Generado: {datetime.now()}\n\n")
    f.write("--- Datos leídos desde Windows ---\n")
    f.write(contenido + "\n")
    f.write("--- Datos de Ubuntu ---\n")
    f.write(f"Memoria: {info_ubuntu}\n")

print(f"\n✅ Reporte combinado guardado en Ubuntu:")
print(f" {ruta_destino}")
print(f" También visible en Windows: \\\\wsl$\\Ubuntu{ruta_destino}")
