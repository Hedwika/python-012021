import pandas
import wget

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")
twilio = pandas.read_csv('twlo.csv')

print(twilio.shape)

print(twilio.iloc[:5])
print(twilio.head())
print(twilio.iloc[301])

pocet_radku = twilio.shape[0]
print(f"Tabulka má {pocet_radku} řádků.")

prvni_hodnota = twilio.iloc[0, 5]
posledni_hodnota = twilio.iloc[301, 5]
rust = int((posledni_hodnota/prvni_hodnota)*100)
print(f"Hodnota akcie se zvýšila o {rust} %.")

nejnizsi_hodnota = twilio["Low"].min()
nejvyssi_hodnota = twilio["High"].max()
price_rance = nejvyssi_hodnota - nejnizsi_hodnota
print(f"Maximální rozsah obchodní ceny akcie je {int(price_rance)} dolarů.")