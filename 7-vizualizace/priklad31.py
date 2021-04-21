# Vrať se k práci se souborem temperature.csv, který obsahuje informace o průměrné teplotě v různých městech v listopadu 2017.

import pandas
import wget
import pytemperature

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

# Vyfiltruj si informace o teplotách 13. listopadu 2017.
temperature = pandas.read_csv('temperature.csv')
temperature["AvgTemperatureCelsius"] = pytemperature.f2c(temperature["AvgTemperature"])
november_13 = temperature.loc[(temperature["Day"] == 13)]

# Vyřaď všechny záznamy, které mají teplotu -99, protože tato hodnota je pravděpodobně chybná.
november_13 = november_13[november_13.AvgTemperature != -99.0]

# Seřad hodnoty v souboru podle teploty od největší po nejmenší.
november_13_ascending = november_13.sort_values(by="AvgTemperature", ascending=False)

# Vypiš pět měst s nejvyšší teplotou a pět měst s nejnižší teplotou
print(f"\n\nNejvyšší teplota byla 13. 11. 2017 v těchto městech:\n{november_13_ascending['City'].head(5)}")
print(f"\n\nNejnižší teplota byla 13. 11. 2017 v těchto městech:\n{november_13_ascending['City'].tail(5)}")