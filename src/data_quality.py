import pandas as pd
import os

# Ruta del csv mas reciente
folder = 'data/raw/'
archivos = sorted([f for f in os.listdir(folder) if f.endswith(".csv")], reverse=True)
archivo = os.path.join(folder, archivos[0])

# Cargar datos
df = pd.read_csv(archivo)

# 1. Resumen general
print("\n Estrcutura General:")
print(df.info())

#2. Mostrar valores nulos
print("\n Valores nuelos por columna: ")
print(df.isnull().sum())

#3. Mostrar duplicados
duplicados = df.duplicated().sum()
print(f"\n Registros de duplicados: {duplicados}")

# 4. Altitud inválida (baro_altitude < 0 o demasiado alta)
altitud_invalida = df[(df['baro_altitude'] < 0) | (df['baro_altitude'] > 20000)]
print(f"\n Altitudes sospechosas: {len(altitud_invalida)} registros")
if not altitud_invalida.empty:
    print(altitud_invalida[['icao24', 'baro_altitude']].head())

# 5. Valores inconsistentes en la columna on_ground
if df['on_ground'].dropna().isin([True, False]).all():
    print("\n Columna 'on_ground' válida (solo True/False).")
else:
    print("\n Valores inesperados en 'on_ground':")
    print(df['on_ground'].value_counts())

# 6. Pais sin definir
print("\n Países de origen nulos o vacíos:")
print(df[df['origin_country'].isnull() | (df['origin_country'].str.strip() == '')].shape[0])
