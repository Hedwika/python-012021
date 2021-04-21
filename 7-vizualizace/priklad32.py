# Stáhni si znovu soubor platy_2021_02.csv s informacemi o platech v softwarové firmě, se kterými jsme již pracovali v příkladu 26.

import wget
import pandas
import matplotlib.pyplot as plt
import pandas as pd

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")

# Načti si tato data do tabulky a vytvoř histogram. Nastav vhodně hranice skupin histogramu (parametr bins), aby byl graf přehledný a snadno interpretovatelný.
platy = pandas.read_csv('platy_2021_02.csv')
platy_bez_cz = platy.drop(['cislo_zamestnance'], axis = 1)
platy_bez_cz.hist(bins=[30_000, 35_000, 40_000, 45_000, 50_000, 55_000, 60_000, 65_000])
plt.show()

# Dobrovolný doplněk
# Vyzkoušej si vytvořit podgrafy. pandas a matplotlib to umí poměrně jednoduše a to pomocí parametru by metody hist(). Jako parametr vlož sloupec, podle kterého chceš data do podgrafů rozdělit. Musíš vložit sloupec ve formě dat, nikoli pouze jeho název.
# Vytvoř pro zadaná data podgrafy pro jednotlivá města. Načti si informace o městě, ve kterém jednotliví pracovníci pracují (to jsme již dělali v příkladu) příkladu 26. Následně sloupec mesto použij na rozdělení podgrafů.
praha = pandas.read_csv('zam_praha.csv')
praha["město"] = "Praha"

plzen = pandas.read_csv('zam_plzeň.csv')
plzen["město"] = "Plzeň"

liberec = pandas.read_csv('zam_liberec.csv')
liberec["město"] = "Liberec"

zamestnanci = pandas.concat([praha, plzen, liberec], ignore_index=True)
df = pd.DataFrame(zamestnanci)
df.to_csv('zamestnanci.csv')

zamestnanci_platy = pandas.merge(zamestnanci, platy, on=['cislo_zamestnance'])
zamestnanci_platy[["město", "plat"]].hist(bins=[30_000, 35_000, 40_000, 45_000, 50_000, 55_000, 60_000, 65_000], by="město")
plt.show()

