import os.path
from os import path
import csv
from datetime import datetime

def rewrite():
    file = open('database.csv', 'w+', newline='')
    with file:
        myfile = csv.writer(file)
        myfile.writerow(["Datum en Tijd", "Naam", "Station", "Bericht"])



def exists():
    if path.exists("database.csv"):
        return True
    else:
        file = open('database.csv', 'w+', newline='')
        with file:
            myfile = csv.writer(file)
            myfile.writerow(["Datum en Tijd", "Naam", "Station", "Bericht"])
        return False
exists()



def berichtmaken():

    with open('database.csv', 'a+', newline='') as file:
        myfile = csv.writer(file)
        nu = datetime.now()
        DatumEnTijd = nu.strftime("%d/%m/%Y ; %H:%M")
        name = input('Voer hier uw naam in:')


        if name == '':
            name = 'Anoniem'
            print('Er is geen naam ingevoerd, dus er wordt voor de naam "Anoniem" gekozen.')


        stationnaam = input('Voer hier de naam van de locatie van het station in:')
        stationslijst = ['Utrecht', 'Amsterdam', 'Boxtel']

        if stationnaam not in stationslijst:
            print("Er is niet voor een juiste stationnaam gekozen.")
            berichtmaken()
            quit()



        bericht = str(input('Voer hier uw bericht in:'))

        if bericht == ' ':
            print("Er is geen bericht ingevoerd.")

        if len(bericht) > 140:
            print("U heeft het maximaal karakters overschreden")
            rewrite()
            berichtmaken()



        myfile.writerow([DatumEnTijd, name, stationnaam, bericht])
doorgaan = True
while doorgaan:
    berichtmaken()
    x = input('Wilt u nog een bericht achterlaten?')
    if x == 'nee':
        doorgaan = False