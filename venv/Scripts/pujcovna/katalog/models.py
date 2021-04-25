from django.db import models

class Auto(models.Model):
    registracni_znacka = models.CharField(max_length=6)
    znacka_a_typ = models.CharField(max_length=100)
    pocet_najetych_km = models.IntegerField()
    datum_posledni_technicke = models.DateField()

class Zakaznik(models.Model):
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    cislo_ridicskeho_prukazu = models.CharField(max_length=15)
    datum_narozeni = models.DateField()

class Vypujcka(models.Model):
    zacatek = models.DateTimeField()
    konec = models.DateTimeField()
    cena = models.IntegerField()