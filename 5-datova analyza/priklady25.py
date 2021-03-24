import pandas
import pandas as pd
import wget
import pytemperature

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
temperature = pandas.read_csv('temperature.csv')

temperature["AvgTemperatureCelsius"] = pytemperature.f2c(temperature["AvgTemperature"])

print(temperature.head())

november_13 = temperature.loc[(temperature["Day"] == 13)]
print(november_13)

november_13_us = temperature.loc[(temperature["Day"] == 13) & (temperature["Country"] == "US")]
df = pd.DataFrame(november_13_us)
print(november_13_us)
df.to_csv('november_13_us.csv')

n_13_us_cities = pandas.read_csv('november_13_us.csv')

washington_philadelphia = n_13_us_cities.loc[((n_13_us_cities["City"] == "Washington") | (n_13_us_cities["City"] == "Philadelphia"))]
print(washington_philadelphia)

mean_11_13_us = n_13_us_cities["AvgTemperatureCelsius"]
print(f"Průměrná teplota byla 13. 11. 2017 na území Spojených Států Amerických {round(mean_11_13_us.mean(),2)} stupnů Celsia.")
print(f"Teplotní medián byl 13. 11. 2017 na území Spojených Států Amerických {round(mean_11_13_us.median(),2)} stupnů Celsia.")
print(f"Teplotní rozptyl byl 13. 11. 2017 na území Spojených Států Amerických {round(mean_11_13_us.var(),2)} stupnů Celsia.")