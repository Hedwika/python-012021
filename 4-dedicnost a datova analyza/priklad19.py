from forex_python.converter import CurrencyRates

mena = input("Zadejte kód měny, do které chcete částku převést: ")
pozadovano_v_cilove_mene = int(input("Kolik Kč chcete směnit?"))
prevodnik = CurrencyRates()
cena_v_korunach = prevodnik.convert('CZK', mena, pozadovano_v_cilove_mene)
print(cena_v_korunach)