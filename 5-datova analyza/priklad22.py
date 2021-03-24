import pandas
import wget

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv")
character_deaths = pandas.read_csv('character-deaths.csv')
character_deaths = character_deaths.set_index("Name")

print(character_deaths.columns)

hali = character_deaths.loc["Hali"]
print(hali)

gavin_gillam = character_deaths.loc["Gevin Harlaw": "Gillam"]
print(gavin_gillam)

gavin_gillam_death_year = character_deaths.loc["Gevin Harlaw": "Gillam", ["Death Year"]]
print(gavin_gillam_death_year)

gavin_gillam_books = character_deaths.loc["Gevin Harlaw": "Gillam", ["GoT", "CoK", "SoS", "FfC", "DwD"]]
print(gavin_gillam_books)
