class Auto:

    def __init__(self, znacka, typ, km):
        self.znacka = znacka
        self.typ = typ
        self.km = km
        self.volne = True

    def pujc_auto(self):
        if self.volne:
            self.volne = False
            return "Potvrzuji zapůjčení vozidla."
        else:
            return "Vozidlo není k dispozici."

    def get_info(self):
        if self.volne:
            return f"Auto {self.typ} s registrační zančkou {self.znacka} má najeto {self.km} a je volné."
        else:
            return f"Auto {self.typ} s registrační zančkou {self.znacka} má najeto {self.km} a není volné."


peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
skoda = Auto("1P3 4747", "Škoda Octavia", 41253)

pujceni = input("Jakou značku si přejete půjčit? Zadejte prosím ‘Peugeot‘ nebo ‘Škoda‘: ")
if pujceni == "Peugeot" or pujceni == "peugeot":
    print(peugeot.get_info())
    print(peugeot.pujc_auto())
elif pujceni == "Skoda" or pujceni == "skoda":
    print(skoda.get_info())
    print(skoda.pujc_auto())
else:
    print(f"Znacku {pujceni} v nabídce (zatím) nemáme.")

pujceni = input("Jakou značku si přejete půjčit? Zadejte prosím ‘Peugeot‘ nebo ‘Škoda‘: ")
if pujceni == "Peugeot" or pujceni == "peugeot":
    print(peugeot.get_info())
    print(peugeot.pujc_auto())
elif pujceni == "Skoda" or pujceni == "skoda":
    print(skoda.get_info())
    print(skoda.pujc_auto())
else:
    print(f"Znacku {pujceni} v nabídce (zatím) nemáme.")