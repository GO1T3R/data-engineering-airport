from sqlalchemy import create_engine, text
import pandas as pd

# Crear conexión con la base de datos
engine = create_engine('sqlite:///data/vuelos.db')

# Consulta 1: ¿Cuántos vuelos hay actualmente registrados?
query1 = "SELECT COUNT(*) AS total_vuelos FROM vuelos"
result1 = pd.read_sql(query1, engine)
print("Total de vuelos registrados:")
print(result1)

# Consulta 2: ¿Cuántos vuelos por país de origen?
query2 = """
SELECT origin_country, COUNT(*) as cantidad
FROM vuelos
GROUP BY origin_country
ORDER BY cantidad DESC
LIMIT 10
"""
result2 = pd.read_sql(query2, engine)
print("\nTop 10 países con más vuelos registrados:")
print(result2)

# Consulta 3: ¿Cuántos están actualmente en tierra vs en el aire?
query3 = """
SELECT on_ground, COUNT(*) as cantidad
FROM vuelos
GROUP BY on_ground
"""
result3 = pd.read_sql(query3, engine)
print("\nDistribución en tierra vs en el aire:")
print(result3)
