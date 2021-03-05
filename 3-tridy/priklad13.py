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

    def vrat_auto(self, tachometr, dny):
        self.km = self.km + tachometr
        self.volne = True
        if dny < 7:
            cena = 400*dny
        else:
            cena = 300*dny
        return f"Cena za zapůjčení vozidla je {cena} Kč."

    def get_info(self):
        if self.volne:
            return f"Auto {self.typ} s registrační značkou {self.znacka} má najeto {self.km} a je volné."
        else:
            return f"Auto {self.typ} s registrační značkou {self.znacka} má najeto {self.km} a není volné."


peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
skoda = Auto("1P3 4747", "Škoda Octavia", 41253)

pujceni = input("Jakou značku si přejete půjčit? Zadejte prosím ‘Peugeot‘ nebo ‘Skoda‘: ")
if pujceni == "Peugeot" or pujceni == "peugeot":
    print(peugeot.get_info())
    print(peugeot.pujc_auto())
elif pujceni == "Skoda" or pujceni == "skoda":
    print(skoda.get_info())
    print(skoda.pujc_auto())
else:
    print(f"Znacku {pujceni} v nabídce (zatím) nemáme.")
    exit()

najeto = int(input("Zadejte počet kilometrů, které zákazník s autem ujel: "))
doba = int(input("Zadejte počet dní, kolik měl zákazník půjčené auto: "))

if pujceni == "Peugeot" or pujceni == "peugeot":
    print(peugeot.vrat_auto(najeto, doba))
    print(skoda.get_info())
elif pujceni == "Skoda" or pujceni == "skoda":
    print(skoda.vrat_auto(najeto, doba))
    print(skoda.get_info())
else:
    print(f"Znacku {pujceni} v nabídce (zatím) nemáme.")