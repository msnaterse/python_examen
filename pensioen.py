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