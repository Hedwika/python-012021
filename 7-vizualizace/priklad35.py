# Vrať se k práci se souborem temperature.csv, který obsahuje informace o průměrné teplotě v různých městech v listopadu 2017.

import wget
import pandas
import pytemperature
import matplotlib.pyplot as plt

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

# Vytvoř tabulku, která bude obsahovat údaje o teplotě za města Helsinki, Miami Beach a Tokyo.
temperature = pandas.read_csv('temperature.csv')
temperature["AvgTemperatureCelsius"] = pytemperature.f2c(temperature["AvgTemperature"])
helsinki = temperature[(temperature["City"] == "Helsinki") | (temperature["City"] == "Miami Beach") | (temperature["City"] == "Tokyo")]

# Vytvoř krabicový graf a porovnej rozsah teplot v těchto městech.
helsinki = temperature[temperature["City"] == "Helsinki"].drop(['AvgTemperature', 'Region', 'Unnamed: 0', 'Day', 'Country', 'City'], axis = 1).reset_index(drop=True)
helsinki.rename(columns={'AvgTemperatureCelsius': 'Helsinki'}, inplace=True)
miami = temperature[temperature["City"] == "Miami Beach"].drop(['AvgTemperature', 'Region', 'Unnamed: 0', 'Day', 'Country', 'City'], axis = 1).reset_index(drop=True)
miami.rename(columns={'AvgTemperatureCelsius': 'Miami'}, inplace=True)
tokyo = temperature[temperature["City"] == "Tokyo"].drop(['AvgTemperature', 'Region', 'Unnamed: 0', 'Day', 'Country', 'City'], axis = 1).reset_index(drop=True)
tokyo.rename(columns={'AvgTemperatureCelsius': 'Tokyo'}, inplace=True)

helsinki_miami_tokyo_november = pandas.concat([helsinki, miami, tokyo], axis=1)
helsinki_miami_tokyo_november.plot(kind='box', whis=[0, 100])
plt.show()