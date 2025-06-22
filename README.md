# ✈️ Proyecto de Ingeniería de Datos: Monitoreo de Vuelos

Este proyecto simula un **pipeline de ingeniería de datos** para obtener información en tiempo real sobre vuelos aéreos utilizando una API pública. Los datos son extraídos, transformados, almacenados en una base de datos y luego validados con métricas de calidad. Además, se genera un reporte interactivo en HTML para análisis exploratorio.

---

## 🧰 Tecnologías Utilizadas

- 🐍 Python 3.8+
- 🗃 SQLite (base de datos local)
- 📦 pandas
- 📊 ydata-profiling (antes pandas-profiling)
- 🛠 SQLAlchemy

---

## 🚀 Componentes del Pipeline

| Script | Descripción |
|--------|-------------|
| `extract_vuelos.py` | Extrae datos desde la API pública de OpenSky |
| `load_to_sqlite.py` | Carga los datos transformados en SQLite |
| `data_quality_check.py` | Realiza validaciones de calidad: nulos, duplicados, valores anómalos |
| `html_data_report.py` | Genera un reporte interactivo en HTML con estadísticas y advertencias |

---

## 📊 Reporte de Calidad de Datos

📁 El proyecto genera automáticamente un reporte HTML que analiza la estructura, estadísticas, valores faltantes y outliers.

🔗 Puedes ver un ejemplo generado aquí:  
[`reporte_calidad_vuelos.html`](./data/processed/reporte_calidad_vuelos.html)

---

## 📁 Estructura del Proyecto

```none
data_engineering_airport/
│
├── data/
│   ├── raw/                # Datos crudos descargados desde la API
│   ├── processed/          # Reportes generados (HTML) y salidas transformadas
│   └── vuelos.db           # Base de datos SQLite con los datos limpios
│
├── src/                    # Código fuente del pipeline
│   ├── extract_vuelos.py
│   ├── load_to_sqlite.py
│   ├── data_quality_check.py
│   └── html_data_report.py
│
├── sql/                    # (Opcional) Scripts SQL o consultas personalizadas
│
├── requirements.txt        # Dependencias
├── .gitignore              # Archivos ignorados por Git
└── README.md               # Documentación del proyecto
```

## 📝 Cómo Ejecutar

```bash
# Clona el repositorio
git clone https://github.com/GO1T3R/data-engineering-airport.git
cd data-engineering-airport

# Crea entorno virtual (opcional)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instala dependencias
pip install -r requirements.txt

# Ejecuta el pipeline manualmente
python src/extract_vuelos.py
python src/load_to_sqlite.py
python src/data_quality_check.py
python src/html_data_report.py

