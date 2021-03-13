from datetime import datetime


class Kontakt:
    def __init__(self, jmeno, email):
        self.jmeno = jmeno
        self.email = email


class Uchazec(Kontakt):
    def __init__(self, jmeno, email, datum_pohovoru):
        super(Uchazec, self).__init__(jmeno, email)
        self.datum_pohovoru = datum_pohovoru
        self.zapis_z_pohovoru = ""

    def uloz_zapis(self, zapis_z_pohovoru):
        aktualni_datum = datetime.now()
        datum_pohovoru = datetime.strptime(self.datum_pohovoru, "%d. %m. %Y")
        if aktualni_datum >= datum_pohovoru:
            self.zapis_z_pohovoru = zapis_z_pohovoru
            return f"Zápis z pohovoru s uchazečem {self.jmeno} byl uložen."
        else:
            return f"Pohovor s uchazečem {self.jmeno} proběhne {self.datum_pohovoru}."


jana = Uchazec("Jana Nováková", "jana.novakova@seznam.cz", "15. 6. 2021")
print(jana.uloz_zapis("nedostavila se."))
jan = Uchazec("Jan Novák", "jan.novak@seznam.cz", "15. 2. 2021")
print(jan.uloz_zapis("bylo to fajn."))
