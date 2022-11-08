import tkinter as tk
import psycopg2
from tkinter import ttk
from tkinter import *




conn = psycopg2.connect(database="stationszuil1",
                                     user="postgres",
                                     password="archena31",
                                     host="localhost")

root = tk.Tk()
root.geometry("800x700")
root.title("Stationszuil")


def openutrecht():
    top = Toplevel()
    top.title('Stationszuil')
    top.geometry("800x600")
    tk.Label(top, text='Station Utrecht', font=('Times', 24)).pack(padx=30, pady=30)
    # Separator object
    separator = ttk.Separator(top, orient='horizontal')
    separator.place(relx=0, rely=0.17, relwidth=1, relheight=1)
    cursor = conn.cursor()
    cursor.execute("select naam, berichtreiziger from bericht where station = 'Utrecht' ORDER BY datumentijd ASC LIMIT 5;")
    results = cursor.fetchall()
    conn.commit()

    for result in results:
        naam1 = result[0]
        bericht1 = result[1]
        yes = tk.Label(top, text=f"{bericht1} ~ {naam1}", font=('Times bold', 10)).pack(padx=30, pady=35)

    import requests, json
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = "Utrecht,NL"
    API_KEY = "5ead39c06cef4059347751de13254b99"
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperatuur = main['temp']
        vochtigheid = main['humidity']
        druk = main['pressure']
        report = data['weather']
        celsius = temperatuur - 273
        celsius = int(celsius)
    else:
        print("Error in the HTTP request")
    weerB = tk.Label(top, text=(f"{CITY:-^30} \n"
                                 f"Temperatuur: {celsius} graden celsius\n"
                                 f"Vochtigheid: {vochtigheid}\n"
                                 f"Luchtdruk: {druk}\n"
                                 f"Weer bericht: {report[0]['description']}"))
    weerB.place(x=60, y=20)
    faciliteit = tk.Label(top, text=(f"Beschikbare faciliteiten:\n"
                       f"OV-Fiets\n"
                       f"Toilet"))
    faciliteit.place(x=650, y=40)



def openamsterdam():
    top = Toplevel()
    top.title('Stationszuil')
    top.geometry("800x600")
    tk.Label(top, text='Station Amsterdam', font=('Times', 24)).pack(padx=30, pady=30)
    separator = ttk.Separator(top, orient='horizontal')
    separator.place(relx=0, rely=0.17, relwidth=1, relheight=1)
    cursor = conn.cursor()
    cursor.execute("select naam, berichtreiziger FROM bericht WHERE station = 'Amsterdam' ORDER BY datumentijd ASC LIMIT 5;")
    results = cursor.fetchall()
    conn.commit()

    for result in results:
        naam1 = result[0]
        bericht1 = result[1]
        yes = tk.Label(top, text=f"{bericht1} ~ {naam1}", font=('Times bold', 10)).pack(padx=30, pady=35)

    import requests, json
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = "Amsterdam,NL"
    API_KEY = "5ead39c06cef4059347751de13254b99"
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperatuur = main['temp']
        vochtigheid = main['humidity']
        druk = main['pressure']
        report = data['weather']
        celsius = temperatuur - 273
        celsius = int(celsius)
    else:
        print("Error in the HTTP request")
    weerB = tk.Label(top, text=(f"{CITY:-^30} \n"
                                f"Temperatuur: {celsius} graden celsius\n"
                                f"Vochtigheid: {vochtigheid}\n"
                                f"Luchtdruk: {druk}\n"
                                f"Weer bericht: {report[0]['description']}"))
    weerB.place(x=60, y=20)
    faciliteit = tk.Label(top, text=(f"Beschikbare faciliteiten:\n"
                                     f"Lift\n"
                                     f"P+R"))
    faciliteit.place(x=650, y=40)

def openboxtel():
    top = Toplevel()
    top.title('Stationszuil')
    top.geometry("800x600")
    tk.Label(top, text='Station Boxtel  ', font=('Times', 24)).pack(padx=30, pady=30)
    separator = ttk.Separator(top, orient='horizontal')
    separator.place(relx=0, rely=0.17, relwidth=1, relheight=1)
    cursor = conn.cursor()
    cursor.execute("select naam, berichtreiziger FROM bericht WHERE station = 'Boxtel' ORDER BY datumentijd ASC LIMIT 5;")
    results = cursor.fetchall()
    conn.commit()

    for result in results:
        naam1 = result[0]
        bericht1 = result[1]
        yes = tk.Label(top, text=f"{bericht1} ~ {naam1}", font=('Times bold', 10)).pack(padx=30, pady=35)

    import requests, json
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = "Boxtel,NL"
    API_KEY = "5ead39c06cef4059347751de13254b99"
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperatuur = main['temp']
        vochtigheid = main['humidity']
        druk = main['pressure']
        report = data['weather']
        celsius = temperatuur - 273
        celsius = int(celsius)
    else:
        print("Error in the HTTP request")
    weerB = tk.Label(top, text=(f"{CITY:-^30} \n"
                                f"Temperatuur: {celsius} graden celsius\n"
                                f"Vochtigheid: {vochtigheid}\n"
                                f"Luchtdruk: {druk}\n"
                                f"Weer bericht: {report[0]['description']}"))
    weerB.place(x=60, y=20)
    faciliteit = tk.Label(top, text=(f"Beschikbare faciliteiten:\n"
                                     f"OV-Fiets\n"
                                     f"Toilet"))
    faciliteit.place(x=650, y=40)


logo = tk.Label(root, text='Kies hier het station uit', font=('Times', 24)).pack(padx=30, pady=30)


separator = ttk.Separator(root, orient='horizontal')
separator.place(relx=0, rely=0.17, relwidth=1, relheight=1)
button1 = Button(root, text="Open Utrecht", command=openutrecht)
button1.place(x=360, y=200)

separator = ttk.Separator(root, orient='horizontal')
separator.place(relx=0, rely=0.40, relwidth=1, relheight=1)
naamstation1 = tk.Label(root, text='Station Utrecht', font=('Helvetica', 11))
naamstation1.place(x=350, y=150)

separator = ttk.Separator(root, orient='horizontal')
separator.place(relx=0, rely=0.64, relwidth=1, relheight=1)
naamstation2 = tk.Label(root, text='Station Amsterdam', font=('Helvetica', 11))
naamstation2.place(x=340, y=300)
button2 = Button(root, text="Open Amsterdam", command=openamsterdam)
button2.place(x=350, y=357)

naamstation3 = tk.Label(root, text='Station Boxtel', font=('Helvetica', 11))
naamstation3.place(x=350, y=500)
button2 = Button(root, text="Open Boxtel", command=openboxtel)
button2.place(x=360, y=550)














root.mainloop()





