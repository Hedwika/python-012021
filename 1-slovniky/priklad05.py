prodeje2019 = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565
}

prodeje2020 = {
    "Zkus mě chytit": 3157,
    "Vrah zavolá v deset": 3541,
    "Vražda podle knihy": 2510,
    "Past": 2364,
    "Zločinný steh": 5412,
    "Zkus mě chytit": 6671,
}

print("Zadejte název knihy, jejíž prodeje vás zajímají: ")
nazev = input()

if nazev in prodeje2019:
    if nazev in prodeje2020:
        print(f"Knihy se prodalo {prodeje2019[nazev] + prodeje2020[nazev]} ks.")
    else:
        print(f"Knihy se prodalo {prodeje2019[nazev]} ks.")
else:
    if nazev in prodeje2020:
        print(f"Knihy se prodalo {prodeje2020[nazev]} ks.")
    else:
        print("Kniha není v seznamu.")