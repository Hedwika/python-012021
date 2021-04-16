import pandas
import pandas as pd
import wget

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")

# Načti data o zaměstnancích z CSV souborů do tabulek (DataFrame). Ke každé tabulce přidej nový sloupec mesto, které bude obsahovat informaci o tom, ve kterém městě zaměstnanec pracuje.
praha = pandas.read_csv('zam_praha.csv')
praha["město"] = "Praha"

plzen = pandas.read_csv('zam_plzeň.csv')
plzen["město"] = "Plzeň"

liberec = pandas.read_csv('zam_liberec.csv')
liberec["město"] = "Liberec"

# Vytvoř novou tabulku zamestnanci a ulož do ní informace o všech zaměstnancích.
zamestnanci = pandas.concat([praha, plzen, liberec], ignore_index=True)
df = pd.DataFrame(zamestnanci)
df.to_csv('zamestnanci.csv')
# V tuto chvíli není nutné ukládat nový soubor, vytvářím ho až zpětně - pracuji teď na doplňku k příkladu 27, kde se mi taková tabulka hodí víc, než abych znova spojovala a načítala tři tabulky původní.

# Ze souboru platy_2021_02.csv načti platy zaměstnanců za únor 2021. Propoj tabulku (operace join) s platy a tabulku se zaměstnanci pomocí sloupce cislo_zamestnance.
platy = pandas.read_csv('platy_2021_02.csv')
zamestnanci_platy = pandas.merge(zamestnanci, platy, on=['cislo_zamestnance'])
print(zamestnanci_platy)

# Porovnej rozměry tabulek před spojením a po spojení. Pokud nemá některý zaměstnanec plat za únor, znamená to, že v naší firmě již nepracuje.
print(zamestnanci.shape)
print(zamestnanci_platy.shape)

# Spočti průměrný plat zaměstnanců v jednotlivých kancelářích.
prumerny_plat = zamestnanci_platy.groupby('město')['plat'].mean()
print(f"\nPrůměrné platby v jednotlivých městech jsou:\n{prumerny_plat}")

# Ulož do proměnné počet zaměstnaců, kteří v naší firmě již nepracují.
odesli = pandas.merge(zamestnanci, platy, on=['cislo_zamestnance'], how="outer")
odesli_pocet = odesli[odesli["plat"].isnull()]
print(f"\nPočet zaměstnanců, kteří v lednu skončili, je {len(odesli_pocet)}.")

# V rámci úspory se IT oddělení rozhodlo prověřit licence přidělené zaměstnancům, kteří ve firmě již nepracují. Vytvoř samostatnou tabulku, která obsahuje jména zaměstnanců, kteří ve firmě již nepracují. Tabulku ulož do souboru CSV.
df = pd.DataFrame(odesli_pocet)
df.to_csv('nepracuji.csv')