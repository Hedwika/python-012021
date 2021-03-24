import pandas
import wget
import pytemperature

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
temperature = pandas.read_csv('temperature.csv')

print(temperature.head())

prague = temperature[(temperature["City"] == "Prague")]
print(prague)

more_than_eighty = temperature[(temperature["AvgTemperature"] > 80)]
print(more_than_eighty)

more_than_sixty_europe = temperature[(temperature["AvgTemperature"] > 60) & (temperature["Region"] == "Europe")]
print(more_than_sixty_europe)

extreme = temperature[(temperature["AvgTemperature"] < -20) | (temperature["AvgTemperature"] > 80)]
print(extreme)

temperature["AvgTemperatureCelsius"] = pytemperature.f2c(temperature["AvgTemperature"])

more_than_thirty_celsius = temperature[(temperature["AvgTemperatureCelsius"] > 30)]
print(more_than_thirty_celsius)

more_than_fifteen_celsius_europe = temperature[(temperature["AvgTemperatureCelsius"] > 15) & (temperature["Region"] == "Europe")]
print(more_than_fifteen_celsius_europe)

extreme_c = temperature[(temperature["AvgTemperatureCelsius"] > 30) | (temperature["AvgTemperature"] < -10)]
print(extreme_c)