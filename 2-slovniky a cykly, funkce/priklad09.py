vysledky = [
  {"Jméno": "Mirek Dušín", "Český jazyk": 1, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 1, "Zeměpis": 1},
  {"Jméno": "Jarka Metelka", "Český jazyk": 3, "Anglický jazyk": 1, "Matematika": 3, "Dějepis": 2, "Ekonomika": 5},
  {"Jméno": "Jindra Hojer", "Český jazyk": 2, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 3, "Chemie": 3},
  {"Jméno": "Červenáček", "Český jazyk": 1, "Anglický jazyk": 1, "Matematika": 1, "Fyzika": 2, "Informatika": 4},
  {"Jméno": "Rychlonožka", "Český jazyk": 4, "Anglický jazyk": 3, "Matematika": 2, "Chemie": 1, "Biologie": 4},
]

found = False
znamkyStudenta = {}


def ohodnotStudenta(znamkyStudenta):
    soucet = 0
    for key, value in znamkyStudenta.items():
        soucet += value
    prumernaZnamka = soucet / len(student)
    if prumernaZnamka <= 1.5:
        if 3 not in student.values():
            return "Prospěl s vyznamenáním."
        else:
            return "Prospěl."
    elif 5 in student.values():
        return "Neprospěl."
    else:
        return "Prospěl."


jmenoStudenta = input("Zadejte jméno studenta: ")

for student in vysledky:
    if student["Jméno"] == jmenoStudenta:
        znamkyStudenta = student
        student.pop("Jméno")
        found = True
        print(ohodnotStudenta(student))

if not found:
    print("Neznámý student.")

