from django.db import models
from datetime import datetime, date
from django.utils import timezone
from django.utils.timezone import is_aware

class Auto(models.Model):
    registracni_znacka = models.CharField(max_length=6)
    znacka_a_typ = models.CharField(max_length=100)
    pocet_najetych_km = models.IntegerField()
    datum_posledni_technicke = models.DateField()

    def __str__(self):
        return str(self.znacka_a_typ)

    @property
    def technicka(self):
        date_format = "%Y-%m-%d"
        a = datetime.strptime(str(datetime.now().date()), date_format)
        b = datetime.strptime(str(self.datum_posledni_technicke), date_format)
        delta = a - b
        return delta.days

class Zakaznik(models.Model):
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    cislo_ridicskeho_prukazu = models.CharField(max_length=15)
    datum_narozeni = models.DateField()
    vypujcka = models.ForeignKey("Vypujcka", on_delete=models.SET_NULL, null=True)
    PROGRAM = (
        ('B', 'Běžný program'),
        ('Z', 'Zlatý program'),
        ('P', 'Platinový program')
    )
    vernostni_program = models.CharField(max_length=1, choices=PROGRAM, null=True)

    def __str__(self):
        return self.jmeno.__str__() + ' ' + self.prijmeni.__str__()

class Vypujcka(models.Model):
    zacatek = models.DateTimeField()
    konec = models.DateTimeField()
    cena = models.IntegerField()
    auto = models.ForeignKey("Auto", on_delete=models.SET_NULL, null=True)

    # def __str__(self):
    #     return self.auto

    @property
    def cas(self):
        zacatek = (self.zacatek).date()
        konec = (self.konec).date()
        if zacatek > date.today():
            return "Výpůjčka proběhne v budoucnosti."
        elif (zacatek < date.today()) & (konec > date.today()):
            return "Výpůjčka právě probíhá."
        else:
            return "Výpůjčka proběhla v minulosti"