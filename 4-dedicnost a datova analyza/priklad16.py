class Polozka:
    def __init__(self, nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr

    def get_info(self):
        return f"Tato položka má název {self.nazev} a je z žánru {self.zanr}."


class Film(Polozka):
    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = delka

    def get_info(self):
        return super().get_info() + f" Délka filmu je {self.delka} minut."


class Serial(Polozka):
    def __init__(self, nazev, zanr, pocet_epizod, delka_epizody):
        super().__init__(nazev, zanr)
        self.pocet_epizod = pocet_epizod
        self.delka_epizody = delka_epizody

    def get_info(self):
        return super().get_info() + f" Počet epizod je {self.pocet_epizod}. Délka jedné epizody je {self.delka_epizody}."



Bandersnatch = Film("Black Mirror - Bandersnatch", "sci-fi", 158)
print(Bandersnatch.get_info())
blackmirror = Serial("Black Mirror", "sci-fi", 18, 62)
print(blackmirror.get_info())