import psycopg2
from datetime import datetime
import csv

conn = psycopg2.connect(
    database = "stationszuil1",
    user = 'postgres',
    password = 'archena31',
    host = 'localhost',
    port = '5432'
)
def berichtschrijven():
    datumtijdunformat = datetime.now()
    datumtijdformatgoedkeuring = datumtijdunformat.strftime("%d/%m/%Y ; %H:%M")
    cursor = conn.cursor()
    query = """INSERT INTO bericht (datumentijd, naam, station, berichtreiziger, datumtijdgoedkeuring) VALUES (%s, %s, %s, %s, %s)"""
    data = (datumtijd, naam, station, bericht, datumtijdformatgoedkeuring)
    cursor.execute(query, data)
    conn.commit()



def rewrite():
    file = open('database.csv', 'w+', newline='')
    with file:
        myfile = csv.writer(file)
        myfile.writerow(["Datum en Tijd", "Naam", "Station", "Bericht"])


def lees_berichten():
   with open('database.csv', 'r') as f:
      uitlezen = f.readlines()
      berichten = uitlezen[1:]
   return berichten

def berichten_opschonen(berichten):
   schoneberichten = []

   for bericht in berichten:
      opschonen = bericht.strip('\n').split(',')

      schoneberichten.append(opschonen)
   return schoneberichten

berichten = lees_berichten()
schoneberichten = berichten_opschonen(berichten)

for bericht in schoneberichten:
    datumtijd, naam, station, bericht = bericht[0], bericht[1], bericht[2], bericht[3]
    print(f"Op {datumtijd} plaatste {naam} voor station {station}")
    print(f"Het bericht: {bericht}")

    goedkeuren = input('Wil je dit bericht goedkeuren?: (Typ ja of nee) ')


    if goedkeuren.lower() == 'ja':
        berichtschrijven()


    if goedkeuren.lower() == 'nee':
        afgekeurd = []
        afgekeurd.append(schoneberichten)
rewrite()