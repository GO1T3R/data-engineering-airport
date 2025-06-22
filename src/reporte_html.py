import pandas as pd
import os
from ydata_profiling import ProfileReport

import pandas as pd
import os
from ydata_profiling import ProfileReport

# Ruta del último archivo CSV
folder = "data/raw/"
archivos = sorted([f for f in os.listdir(folder) if f.endswith('.csv')], reverse=True)

if not archivos:
    raise FileNotFoundError("No hay archivos CSV en data/raw/. Ejecuta primero extract_vuelos.py")

archivo_csv = os.path.join(folder, archivos[0])
df = pd.read_csv(archivo_csv)

# Crear perfil del reporte
profile = ProfileReport(df, title="Reporte de Calidad de Datos: Vuelos", explorative=True)

# Guardar como HTML
output_path = "data/processed/reporte_calidad_vuelos.html"
profile.to_file(output_path)

print(f" Reporte generado correctamente en: {output_path}")
