sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

print("Zadejte prosím kód součástky: ")
kod = input()
if kod not in sklad:
    print("Součástka není skladem.")
    quit()

print("Kolik součástek si chce zákazník koupit?")
pocet = int(input())

if kod in sklad:
    if pocet > sklad[kod]:
        print(f"Je možné prodat jen " + str(sklad[kod]) + " ks této součástky.")
        sklad.pop(kod)
    else:
        print("Poptávku lze uspokojit v plné výši.")
        sklad[kod] = (sklad[kod] - pocet)