# Proyecto de Ingeniería de Datos: Monitoreo de Vuelos

Este proyecto simula un pipeline de ingeniería de datos que obtiene datos en tiempo real de vuelos aéreos, los transforma y los almacena en una base de datos, realizando validaciones de calidad y generando reportes visuales.

## 🔧 Tecnologías
- Python
- SQLite
- pandas
- ydata-profiling
- SQLAlchemy

## 🚀 Componentes
- `extract_vuelos.py`: Extrae datos desde OpenSky API
- `load_to_sqlite.py`: Carga los datos en SQLite
- `data_quality_check.py`: Valida duplicados, nulos y valores fuera de rango
- `html_data_report.py`: Genera un reporte interactivo de calidad en HTML

## 📊 Reporte de Calidad de Datos
Puedes ver un ejemplo del reporte generado aquí:  
➡️ [`reporte_calidad_vuelos.html`](./data/processed/reporte_calidad_vuelos.html)

## 📂 Estructura
data_engineering_airport/
│
├── data/
│   ├── raw/                          ← CSV descargados desde API
│   ├── processed/                    ← Reportes generados (HTML, etc.)
│   └── vuelos.db                     ← Base de datos SQLite
│
├── src/                              ← Código fuente
│   ├── extract_vuelos.py
│   ├── load_to_sqlite.py
│   ├── data_quality_check.py
│   └── html_data_report.py
│
├── sql/                              ← Consultas SQL o scripts (opcional)
│
├── requirements.txt                  ← Librerías necesarias
├── .gitignore                        ← Archivos/carpetas a excluir
├── README.md                         ← Descripción del proyecto
└── LICENSE (opcional)                ← Licencia de uso si lo harás público
