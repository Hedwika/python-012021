import wget
import pandas

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/staty.json")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/gdp.csv")

# V souboru staty.json jsou uložena data s informacemi o státech světa, se kterými jsme již pracovali. Zkusme nyní zpracovat podobné úlohy pomocí pandas.
# Načti data ze souboru do tabulky.
staty = pandas.read_json('staty.json')

# Vyfiltruj státy, které leží v Evropě.
evropa = staty[(staty["region"] == "Europe")]

# Zjisti počet států v jednotlivých subregionech Evropy.
evropa_subregions = evropa.drop(['alpha2Code', 'alpha3Code', 'capital', 'region', 'population', 'area'], axis = 1)
evropa_subregions = evropa_subregions.rename(columns={'name': 'count'})
subregiony_evropy = evropa_subregions.groupby('subregion')
print(subregiony_evropy.count())

# Zjisti cekový počet obyvatel v jednotlivých subregionech Evropy.
evropa_population = evropa.drop(['alpha2Code', 'alpha3Code', 'capital', 'region', 'name', 'area'], axis = 1)
populace_evropy = evropa_population.groupby('subregion')
print(populace_evropy.sum("population"))

# Rozšíření zadání
# V souboru staty.json jsou uložena data s informacemi o státech světa, se kterými jsme již pracovali. V souboru gdp.csv jsou dále informace o hrubém domácím produktu (Gross Domestic Product - GDP) států za roky 2017-2019 ze Světové banky.
# - Načti informace ze souborů do tabulek. Z tabulky s GDP odeber státy, které nemají kompletní informace GDP (tj. ponech pouze státy, které mají kompletní data za všechny tři roky).
gdp = pandas.read_csv('gdp.csv')
gdp = gdp.dropna()

# - Propoj obě tabulky podle třípísmenného kódu států.
gdp = gdp.rename(columns={'Country Code': 'alpha3Code'})
staty_gdp = pandas.merge(staty, gdp, on=['alpha3Code'])

# - Spočti celkové HDP za rok 2019 a celkový počet obyvatel za jednotlivé subregiony.
subregions_hdp = staty_gdp.drop(['alpha2Code', 'alpha3Code', 'capital', 'region', 'name', 'area', 'population', '2017', '2018'], axis = 1)
subregions_hdp19 = subregions_hdp.groupby('subregion')
print(subregions_hdp19.sum("2019"))

subregions_population = staty_gdp.drop(['alpha2Code', 'alpha3Code', 'capital', 'region', 'name', 'area', '2019', '2017', '2018'], axis = 1)
subregions_total_population = subregions_population.groupby('subregion')
print(subregions_total_population.sum("population"))

# - Projdi si subkapitolu o počítaných sloupcích (část o podmínených sloupcích není nutné číst). K tabulce, kterou jsi vytovřila v předchozím kroku, vypočti GDP v roce 2019 na obyvatele, tj. přidej sloupec s velikostí GDP v roce 2019 vydělenou počtem obyvatel daného subregionu.
subregions_2019_population = staty_gdp.drop(['alpha2Code', 'alpha3Code', 'capital', 'region', 'name', 'area', '2017', '2018'], axis = 1)
subregions_2019_population["GDP per capita"] = abs(subregions_2019_population["2019"] / subregions_2019_population["population"])
subregions_gdp_per_capita = subregions_2019_population.groupby('subregion')
print(subregions_gdp_per_capita.sum())