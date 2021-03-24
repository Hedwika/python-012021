import pandas
import wget

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")
vaccinations = pandas.read_csv('country_vaccinations.csv')

total_vaccinated = vaccinations.loc[(vaccinations["date"] == "2021-03-10"), ["country", "total_vaccinations"]]
print(total_vaccinated)

more_than_million = vaccinations.loc[(vaccinations["date"] == "2021-03-10") & (vaccinations["total_vaccinations"] > 1_000_000), ["country", "total_vaccinations"]]
print(more_than_million)

champions = vaccinations[(vaccinations["date"] == "2021-03-10") & (vaccinations["daily_vaccinations"] > 100_000)]
print(champions)

loosers = vaccinations[(vaccinations["date"] == "2021-03-10") & (vaccinations["daily_vaccinations"] < 100)]
print(champions)

ukfi = vaccinations[((vaccinations["date"] == "2021-03-10") | (vaccinations["date"] == "2021-03-11")) & (vaccinations["country"].isin(["United Kingdom", "Finland", "Italy"]))]
print(ukfi)

japan = vaccinations[((vaccinations["date"] >= "2021-03-03") & (vaccinations["date"] <= "2021-03-09")) & (vaccinations["country"].isin(["Japan"]))]
print(japan)