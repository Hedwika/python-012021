from forex_python.bitcoin import BtcConverter

mena_investice = input("Zadejte kód měny, kterou máte k dispozici: ")
pozadovano_bitcoinu = int(input("Zadejte množství BTC, které chcete koupit: "))

prevodnik = BtcConverter()
mnozstvi_meny = (prevodnik.get_latest_price(mena_investice))*pozadovano_bitcoinu
print(mnozstvi_meny)