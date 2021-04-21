# Stáhni si soubor twlo.csv, který obsahuje informace o vývoji ceny akcie firmy Twilio od začátku roku 2020. Soubor obsahuje informace o otevírací, minimální, maximální a uzavírací ceně za každý den.

import wget
import pandas
import matplotlib.pyplot as plt

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")
twilio = pandas.read_csv("twlo.csv")

# Výše uvedeným programem načti data o vývoji ceny akcie. Vytvoř čárový graf vývoje zavírací ceny akcie (sloupec Close) v čase.
twilio_1 = twilio.drop(['High', 'Open', 'Low', 'Unnamed: 0'], axis=1)
fig = twilio_1.plot(x='Date', grid=True, legend=True)
fig.set_title("Twilio price graph")
fig.set_ylabel("Close price")
fig.set_xlabel("Date")
plt.ylim(0, 500)
plt.show()

# Zkus nyní převést sloupec Date na typ datetime příkazem níže a vytvoř stejný graf jako předtím. Porovnej grafy a zjisti, co se změnilo.
twilio["Date"] = pandas.to_datetime(twilio["Date"])
twilio_2 = twilio.drop(['High', 'Open', 'Low', 'Unnamed: 0'], axis=1)
fig = twilio_2.plot(x='Date', grid=True, legend=True)
fig.set_title("Twilio price graph")
fig.set_ylabel("Close price")
fig.set_xlabel("Date")
plt.ylim(0, 500)
plt.show()
# krásné zobrazení měsíců, mnohem přehlednější

# Dobrovolný doplněk
# Přidej ke grafům popisky os a titulky. Po zavolání funkce plot() si výsledek ulož do proměnné ax. Následně zavolej metodu set_ylabel(), abys nastavila popisek osy y grafu.
# ax = twilio.plot()
# ax.set_ylabel("Cena v dolarech")
# Obdobně využij metody set_title() a set_xlabel() a nastav popisek osy x a titulek grafu.