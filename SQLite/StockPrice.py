import requests
import pandas as pd

#Funktion um die Price von Marketaggregator durch API zu holen. Hier "messari" und Daten sind von Binance.
def get_crypto_price(symbol, start, end):
    api_url = f'https://data.messari.io/api/v1/markets/binance-{symbol}-usdt/metrics/price/time-series?start={start}&end={end}&interval=1d'
    raw = requests.get(api_url).json()
    dataframe = pd.DataFrame(raw['data']['values'])# Erhaltene Datei in file Dataframe zu speichern
    dataframe = dataframe.rename(columns = {0:'date',1:'open',2:'high',3:'low',4:'close',5:'volume'})# Spalten unbennenen
    dataframe['date'] = pd.to_datetime(dataframe['date'], unit = 'ms')
    dataframe = dataframe.set_index('date')
    return dataframe

dataframe = get_crypto_price('eth', '2020-01-01', '2023-01-01') # Symbol von Währung und Zeitabschnit in Funktion übergeben
#dataframe.to_csv("stock_data.csv")#gespeicherte Datei als .csv speichern
dataframe = dataframe.filter(items=['close', 'date'])# nach bestimmte Daten filtern
dataframe.rename(columns={'date':{'ds'}, 'close':'y'}, inplace=True)# Spalten unbenennen

print(dataframe)