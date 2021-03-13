class Polozka:
    def __init__(self, nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr

    def get_info(self):
        return f"Tato položka má název {self.nazev} a je z žánru {self.zanr}."


class Film(Polozka):
    def __init__(self, nazev, zanr, delka_stopaze):
        super().__init__(nazev, zanr)
        self.delka_stopaze = delka_stopaze

    def get_celkova_delka(self):
        return f"Celková délka filmu je {self.delka_stopaze} minut."

    def get_info(self):
        return super().get_info() + f" Délka filmu je {self.delka_stopaze} minut."


class Serial(Polozka):
    def __init__(self, nazev, zanr, pocet_epizod, delka_epizody):
        super().__init__(nazev, zanr)
        self.pocet_epizod = pocet_epizod
        self.delka_epizody = delka_epizody
        self.delka_stopaze = self.pocet_epizod * self.delka_epizody

    def get_celkova_delka(self):
        hodiny = self.delka_stopaze/60
        return f"Celková délka seriálu je {self.delka_stopaze} minut, to je {hodiny} hodin."

    def get_info(self):
        return super().get_info() + f" Počet epizod je {self.pocet_epizod}. Délka jedné epizody je {self.delka_epizody} minut."


class Uzivatel:
    def __init__(self, uzivatelske_jmeno):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.zhlednute_porady = {}
        self.celkem_zhlednuto = 0

    def zhledni_polozku(self, polozka):
        self.zhlednute_porady[polozka.nazev] = int(polozka.delka_stopaze)
        return f"Uživatel {self.uzivatelske_jmeno} už viděl tyto pořady: {self.zhlednute_porady}."

    def pripocti_zhlednuti(self, polozka):
        self.delka_sledování += polozka.delka_stopaze
        hodiny_sledovani = self.delka_sledování/60
        return f"Uživatel viděl celkem {self.delka_sledování} minut filmů a seriálů, to je {hodiny_sledovani} hodin."

    def delka_sledovani(self):
        for key, value in self.zhlednute_porady.items():
            self.celkem_zhlednuto += value
            celkem_hodin = self.celkem_zhlednuto/60
        return f"Uživatel viděl celkem {self.celkem_zhlednuto} minut filmů a seriálů, to je {celkem_hodin} hodin."

Bandersnatch = Film("Black Mirror - Bandersnatch", "sci-fi", 158)
print(Bandersnatch.get_info())
print(Bandersnatch.get_celkova_delka())
blackmirror = Serial("Black Mirror", "sci-fi", 18, 62)
print(blackmirror.get_info())
print(blackmirror.get_celkova_delka())
pepa = Uzivatel("pepek")
print(pepa.zhledni_polozku(Bandersnatch))
print(pepa.delka_sledovani())
print(pepa.zhledni_polozku(blackmirror))
print(pepa.delka_sledovani())