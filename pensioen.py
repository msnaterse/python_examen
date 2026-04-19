# Functie voor berekening pesioen
def bereken_pensioen(leeftijf, statuut):
    if statuut == "medewerker":
        bedrag = 350
        extra = 20

    elif statuut == "zelfstandige":
        bedrag = 300
        extra = 15

    elif statuut == "ambtenaar":
        bedrag = 370
        extra = 25

    else:
        return -1

    if leeftijd >= 70:
        return bedrag + extra
    elif leeftijd >= 65:
        return bedrag
    else:
        return 0

#Lijst met statuutkeuzes
statuten = ["medewerker","zelfstandige", "ambtenaar"]

#invoer van personeel
leeftijd = int(input("Voer hier uw leeftijd in"))
statuut = input("kies uit: medewerker, zelfstandige of ambtenaar").lower()
