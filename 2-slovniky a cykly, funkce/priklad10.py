def sance(odvetvi, obrat, zeme, konference=False, newsletter=False):
    body = 0

    if odvetvi == "automotive" or odvetvi == "Automotive":
        body += 3
    elif odvetvi == "retail" or odvetvi == "Retail":
        body += 2
    else:
        body += 0

    if int(obrat) <= 10000000:
        body += 0
    elif int(obrat) <= 1000000000:
        body += 3
    else:
        body += 1

    if zeme == "Česko" or zeme == "Slovensko":
        body += 2
    elif zeme == "Německo" or zeme == "Francie":
        body += 1
    else:
        body += 0

    if konference:
        body += 1
    else:
        body += 0

    if newsletter:
        body += 1
    else:
        body += 0

    return body

obor = input("Zadejte obor, ve kterém podniká potancionální zákazník: ")
finance = input("Zadejte obrat potancionálního zákazníka v EUR: ")
misto = input("Zadejte zemi, ve které potancionální zákazník podniká: ")
ucast = input("Zúčastnil se zákazník naší konference? ")
prihlaseni = input("Odebírá potencionální zákazník náš newsletter? ")

if ucast == "Ano" or ucast == "ano":
    if prihlaseni == "Ano" or prihlaseni == "ano":
        print(sance(obor, finance, misto, True, True))
    else:
        print(sance(obor, finance, misto, True, False))
else:
    if prihlaseni == "Ano" or prihlaseni == "ano":
        print(sance(obor, finance, misto, False, True))
    else:
        print(sance(obor, finance, misto, False, False))
