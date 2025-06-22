import pandas as pd
from sqlalchemy import create_engine
import os

# Ruta de los archivos
folder = "data/raw/"
archivos = sorted(os.listdir(folder), reverse=True)

# Verifica que haya al menos un archivo CSV
if not archivos:
    raise FileNotFoundError("No se encontraron archivos en data/raw/. Ejecuta primero extract_vuelos.py")

# Solo usar archivos CSV
archivos_csv = [f for f in archivos if f.endswith('.csv')]

if not archivos_csv:
    raise FileNotFoundError("No se encontraron archivos .csv en data/raw/")

# Selecciona el archivo más reciente
archivo_csv = os.path.join(folder, archivos_csv[0])

# Leer CSV
df = pd.read_csv(archivo_csv)

# Crear conexión SQLite
engine = create_engine('sqlite:///data/vuelos.db')

# Cargar los datos a la base
df.to_sql("vuelos", engine, if_exists="replace", index=False)

print(f"Datos cargados en 'data/vuelos.db', tabla 'vuelos'.")

