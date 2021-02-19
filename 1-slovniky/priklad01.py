baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
print("Zadejte prosím kód balíku: ")
kod = input()
if kod in baliky:
    if baliky[kod] == True:
        print("Balík byl předán kurýrovi.")
    else:
        print("Balík zatím nebyl předán kurýrovi.")
else:
    print("Zadaný kód balíku neexistuje.")