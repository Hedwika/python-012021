# Vrať se k práci se souborem temperature.csv, který obsahuje informace o průměrné teplotě v různých městech v listopadu 2017.

import wget
import pandas
import pytemperature
import matplotlib.pyplot as plt

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

# Vytvoř tabulku, která bude obsahovat údaje o teplotě za města Helsinki, Miami Beach a Tokyo.
temperature = pandas.read_csv('temperature.csv')
temperature["AvgTemperatureCelsius"] = pytemperature.f2c(temperature["AvgTemperature"])
november_13 = temperature.loc[(temperature["Day"] == 13)]
helsinki_miami_tokyo = november_13.loc[((november_13["City"] == "Helsinki") | (november_13["City"] == "Miami Beach") | (november_13["City"] == "Tokyo"))]

# Vytvoř krabicový graf a porovnej rozsah teplot v těchto městech.
helsinki_miami_tokyo_graph = helsinki_miami_tokyo.drop(['AvgTemperature', 'Region', 'Unnamed: 0', 'Day', 'Country'], axis = 1)
helsinki_miami_tokyo_graph.boxplot(whis=[10, 20])
plt.show()