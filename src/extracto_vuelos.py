import requests
import pandas as pd
from datetime import datetime
import time

def extraer_datos_vuelos():
    url = "https://opensky-network.org/api/states/all"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()['states']
        columnas = [
            'icao24', 'callsign', 'origin_country', 'time_position', 'last_contact',
            'longitude', 'latitude', 'baro_altitude', 'on_ground', 'velocity',
            'heading', 'vertical_rate', 'sensors', 'geo_altitude',
            'squawk', 'spi', 'position_source'
        ]

        df = pd.DataFrame(data, columns=columnas)
        df['timestamp'] = datetime.utcnow()

        return df
    else:
        print("Error al obtener los datos:", response.status_code)
        return pd.DataFrame()

if __name__ == "__main__":
    df_vuelos = extraer_datos_vuelos()
    print(df_vuelos.head())
    df_vuelos.to_csv("data/raw/vuelos_" + datetime.utcnow().strftime("%Y%m%d%H%M") + ".csv", index=False)
