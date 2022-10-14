from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
#use databace spiele
db = client.spiele
#use collection pcgames
collection = db.pcgames
#insert data
collection.insert_one({"Titel": "Transportfever","Ausgabejahr": 2016,"Verkaufszahlen": 500000,"Altersgrenze": 0,"Art":["Simulation","Strategie","Wirtschaftssimulation","Bau-Simulation","Verkehrssimulation","Geschicklichkeitsspiel"],"Wertung":10})
collection.insert_one({"Titel": "Transportfever2","Ausgabejahr": 2019,"Verkaufszahlen": 1000000,"Altersgrenze": 0,"Art":["Simulation","Strategie","Wirtschaftssimulation","Bau-Simulation","Verkehrssimulation","Geschicklichkeitsspiel"],"Wertung":9})
collection.insert_one({"Titel": "Trainfever","Ausgabejahr": 2013,"Verkaufszahlen": 250000,"Altersgrenze": 0,"Art":["Simulation","Strategie","Wirtschaftssimulation","Bau-Simulation","Verkehrssimulation","Geschicklichkeitsspiel"],"Wertung":8})
collection.insert_one({"Titel": "GTA V","Ausgabejahr":2013,"Verkaufszahlen":10000000,"Altersgrenze":18,"Art":["Action","Adventure","Open-World","Kampfspiel","Shooter","Multiplayer"],"Wertung":8})
collection.insert_one({"Titel": "HOI4","Ausgabejahr":2016,"Verkaufszahlen":1000000,"Altersgrenze":16,"Art":["Strategie","Weltkriegssimulation","Wirtschaftssimulation","Geschicklichkeitsspiel","Multiplayer"],"Wertung":9})
collection.insert_one({"Titel": "Jurassic World Evolution","Ausgabejahr":2018,"Verkaufszahlen":1000000,"Altersgrenze":12,"Art":["Simulation","Strategie","Wirtschaftssimulation","Bau-Simulation","Geschicklichkeitsspiel","Gruselspiel"],"Wertung":8})
collection.insert_one({"Titel": "Minecraft","Ausgabejahr":2011,"Verkaufszahlen":10000000,"Altersgrenze":0,"Art":["Sandbox","Open-World","Kampfspiel","Multiplayer"],"Wertung":6})
collection.insert_one({"Titel": "Cities Skylines","Ausgabejahr":2015,"Verkaufszahlen":1000000,"Altersgrenze":0,"Art":["Simulation","Strategie","Wirtschaftssimulation","Bau-Simulation","Geschicklichkeitsspiel"],"Wertung":8})
collection.insert_one({"Titel": "Microsoft Flight Simulator","Ausgabejahr":2020,"Verkaufszahlen":100000,"Altersgrenze":0,"Art":["Simulation","Flugsimulation","Geschicklichkeitsspiel"],"Wertung":9})
collection.insert_one({"Titel": "World of Subways Volume 3: London Underground Circle Line","Ausgabejahr":2011,"Verkaufszahlen":"null","Altersgrenze":3,"Art":["Simulation","Lokführersimulation"],"Wertung":5})
collection.insert_one({"Titel": "World of Subways Volume 1: The PATH","Ausgabejahr":2008,"Verkaufszahlen":"null","Altersgrenze":3,"Art":["Simulation","Lokführersimulation"],"Wertung":5})
collection.insert_one({"Titel": "World of Subways Volume 2: U7-Berlin","Ausgabejahr":2009,"Verkaufszahlen":"null","Altersgrenze":3,"Art":["Simulation","Lokführersimulation"],"Wertung":5})
collection.insert_one({"Titel": "World of Subways Volume 4: New York Line 7","Ausgabejahr":2015,"Verkaufszahlen":"null","Altersgrenze":3,"Art":["Simulation","Lokführersimulation"],"Wertung":5})