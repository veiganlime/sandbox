import sqlite3
import pandas as pd

#Tabelle öfnen, ggf. erzeugen
conn = sqlite3.connect(r'D:\workspace_python\Python_Projekte\SQlite\data\SpotifyFeatures.db')
#.csv Datei importieren
dataframe = pd.read_csv('D:\workspace_python\Python_Projekte\SQlite\data\SpotifyFeatures.csv')
#Abfrage von den vorhandenen Spalten und deren types
print(dataframe.dtypes)

# Vorhandenen Spalten von .csv in erzeugte .db umwandeln.
dataframe.to_sql('genre', conn, if_exists='replace', index=False)
dataframe.to_sql('artist_name', conn, if_exists='replace', index=False)
dataframe.to_sql('track_name', conn, if_exists='replace', index=False)
dataframe.to_sql('track_id  ', conn, if_exists='replace', index=False)
dataframe.to_sql('popularity', conn, if_exists='replace', index=False)
dataframe.to_sql('acousticness ', conn, if_exists='replace', index=False)
dataframe.to_sql('danceability', conn, if_exists='replace', index=False)
dataframe.to_sql('duration_ms', conn, if_exists='replace', index=False)
dataframe.to_sql('instrumentalness   ', conn, if_exists='replace', index=False)
dataframe.to_sql('key ', conn, if_exists='replace', index=False)
dataframe.to_sql('liveness ', conn, if_exists='replace', index=False)
dataframe.to_sql('loudness   ', conn, if_exists='replace', index=False)
dataframe.to_sql('mode', conn, if_exists='replace', index=False)
dataframe.to_sql('speechiness', conn, if_exists='replace', index=False)
dataframe.to_sql('tempo', conn, if_exists='replace', index=False)
dataframe.to_sql('time_signature', conn, if_exists='replace', index=False)
dataframe.to_sql('valence', conn, if_exists='replace', index=False)






