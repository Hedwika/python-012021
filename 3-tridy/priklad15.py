from datetime import datetime, timedelta

den = input("Zadejte datum, na které si chcete koupit vstupenky, například ‘23. 8. 2021‘ pro 23. srpna 2021: ")

datum = datetime.strptime(den, "%d. %m. %Y")

cervenecO = datetime(2021, 7, 1)
cervenecZ = datetime(2021, 8, 10)
srpenO = datetime(2021, 8, 11)
srpenZ = datetime(2021, 8, 31)

if datum < cervenecO or datum > srpenZ:
    print("Letní kino je zavřené.")
else:
    osoby = int(input("Kolik vstupenek si chcete koupit? "))
    cenaC = 250
    cenaS = 180
    if datum <= cervenecZ:
        cena = cenaC * osoby
        print(f"Cena za vstupenky je {cena} Kč.")
    else:
        cena = cenaS * osoby
        print(f"Cena za vstupenky je {cena} Kč.")