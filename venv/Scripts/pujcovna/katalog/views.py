from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView
from . import models

class IndexView(View):
    def get(self, request):
        return HttpResponse("""<h1>Vítejte v naší autopůjčovně!</h1>
<a href='http://localhost:8000/katalog/seznam/'>Jaká auta máme?</a><br>
<h2>O naší autopůjčovně</h2>
<p>Naše půjčovna vznikla v roce 2011 a dnes nabízí přibližně 30 aut.</p>
""")

class SeznamAut(ListView):
    model = models.Auto
    template_name = "katalog/seznam_aut.html"

class PrehledVypujcek(ListView):
    model = models.Vypujcka
    template_name = "katalog/prehled_vypujcek.html"

class SeznamZakazniku(ListView):
    model = models.Zakaznik
    template_name = "katalog/seznam_zakazniku.html"