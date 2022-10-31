from ast import If
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
#use databace spiele
db = client.spiele
#use collection pcgames
collection = db.pcgames
#never ending loop
a=1
while a == 1:
    #ask for input
    print("was möchten sie machen? (insert, find, delete, update, exit, hilfe, show all)")
    eingabe = input()
    #insert data
    if eingabe == "insert":
        print("Geben sie den Namen des Spiels ein")
        Titel = input()
        print("Geben sie bitte das Ausgabejahr ein")
        Ausgabejahr = input()
        print("Geben sie bitte die Verkaufszahlen ein")
        Verkaufszahlen = input()
        print("Geben sie bitte die Altersfreigabe ein")
        Altersgenze = input()
        print("Geben sie bitte die Art des Spiels ein")
        Art = input()
        print("Geben sie bitte eine Wertung Von 0 bis 10 ein")
        Wertung = input()
        collection.insert_one({
            "Titel": Titel,
            "Ausgabejahr": Ausgabejahr,
            "Verkaufszahlen": Verkaufszahlen,
            "Altersgrenze": Altersgenze,
            "Art": Art,
            "Wertung": Wertung
            })
        print("Erfolgreich hinzugefügt")
    elif eingabe == "show all":
        for document in collection.find():
            print(document)
    #find data
    elif eingabe == "find":
        print("nach was möchten sie suchen? (Titel, Ausgabejahr, Verkaufszahlen, Altersgrenze, Art, Wertung)")
        suche = input()
        if suche == "Titel":
            print("Geben sie den Titel ein")
            Titel = input()
            for x in collection.find({"Titel": Titel}):
                print(x)
        elif suche == "Ausgabejahr":
            print("Geben sie das Ausgabejahr ein")
            Ausgabejahr = int(input())
            for x in collection.find({"Ausgabejahr": Ausgabejahr}):
                print(x)
        elif suche == "Verkaufszahlen":
            print("Geben sie die Verkaufszahlen ein")
            Verkaufszahlen = int(input())
            for x in collection.find({"Verkaufszahlen": Verkaufszahlen}):
                print(x)
        elif suche == "Altersgrenze":
            print("Geben sie die Altersgrenze ein")
            Altersgrenze = int(input())
            for x in collection.find({"Altersgrenze": Altersgrenze}):
                print(x)
        elif suche == "Art":
            print("Geben sie die Art ein")
            Art = input()
            for x in collection.find({"Art": Art}):
                print(x)
        elif suche == "Wertung":
            print("Geben sie die Wertung ein")
            Wertung = int(input())
            for x in collection.find({"Wertung": Wertung}):
                print(x)
        else:
            print("Falsche Eingabe")
    #delete data
    elif eingabe == "delete":
        print("Bitte geben sie den Namen des Spiels ein")
        name = input()
        collection.delete_one({"Titel": name})
        print("Erfolgreich gelöscht")
    #update data
    elif eingabe == "update":
        print("Bitte geben sie den Namen des Spiels ein")
        name = input()
        print("Was möchten sie ändern? (Titel, Ausgabejahr, Verkaufszahlen, Altersgrenze, Art, Wertung)")
        aendern = input()
        print("Bitte geben sie den neuen Wert ein")
        neu = input()
        collection.update_one({"Titel": name}, {"$set": {aendern: neu}})
        print("Erfolgreich geändert")
    #exit program
    elif eingabe == "exit":
        print("Programm wird beendet")
        exit()
    #help
    elif eingabe == "hilfe":
        print("insert = Daten einfügen")
        print("find = Daten suchen")
        print("delete = Daten löschen")
        print("update = Daten ändern")
        print("exit = Programm beenden")
        print("hilfe = Hilfe")
        print("version 0.4.2")
        print("produziert am 31.10.2020 12:20")
    #wrong input
    else:
        print("Falsche Eingabe")
        print("Geben sie hilfe ein um die Hilfe anzuzeigen")
    
