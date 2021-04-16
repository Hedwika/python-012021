import wget
import pandas
import pytemperature

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

# Pokud jsi v minulé lekci zpracovala rozšířené zadání, můžeš pracovat s teplotami ve stupních Celsia.
# - Vyfiltruj si informace o teplotách 13. listopadu 2017.
temperature = pandas.read_csv('temperature.csv')
temperature["AvgTemperatureCelsius"] = pytemperature.f2c(temperature["AvgTemperature"])
november_13 = temperature.loc[(temperature["Day"] == 13)]

# - Vyřaď všechny záznamy, které mají teplotu -99, protože tato hodnota je pravděpodobně chybná.
november_13 = november_13[november_13.AvgTemperature != -99.0]

# - Vypočti počet dat, které máš pro daný den za jednotlivé regiony.
insert_count = november_13.drop(['AvgTemperature', 'AvgTemperatureCelsius', 'City', 'Country', 'Day'], axis = 1)
insert_count = insert_count.rename(columns={'Unnamed: 0': 'Počet dat'})
insert_count = insert_count.groupby('Region')
print(insert_count.count())

# - Vypočti průměrnou teplotu za jednotlivé regiony.
average_temperature = november_13.drop(['Unnamed: 0', 'AvgTemperature', 'City', 'Country', 'Day'], axis = 1)
average_temperature= average_temperature.groupby('Region')
print(f"\n\n{average_temperature.mean()}")

# - Vypočti maximální a minimální teplotu v každém regionu.
print(f"\n\n{average_temperature.max()}")
print(f"\n\n{average_temperature.min()}")