volnePokoje = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}
print("Na kterou hodinu si chceš zamluvit meeting room? ")
cas = input()
cas = int(cas)

if cas in volnePokoje:
    if len(volnePokoje[cas]) == 0:
        print("K dispozici je " + str(len(volnePokoje[cas])) + " meeting rooms.")
    else:
        print("K dispozici jsou " + str(len(volnePokoje[cas])) + " meeting rooms.")
else:
    print("Můžeš si zamlouvat meeting room jen od 9 do 12 včetně.")