from json import loads

def nk3(aditza):
    hand = open("nk3.json", "r")
    info = hand.read()
    NK3 = loads(info)
    
    erantzuna = False
    for element in NK3:
        tipo = NK3[element]
        for zenbaki in tipo:
            verbos = tipo[zenbaki]
            for tiempo in verbos:
                pertsonak = verbos[tiempo]
                for pertsona in pertsonak.items():
                    if aditza == pertsona[1]:
                        sujeto = None
                        if tiempo == "Singularra":
                            sujeto = "hura"
                        elif tiempo == "Plurala":
                            sujeto = "haiek"
                        erantzuna = {"Aditza":aditza,"Kasua":"NOR-NORK", "Modua":element, "Denbora":zenbaki, "Nor":sujeto, "Nori":None, "Nork":pertsona[0]}
                        print(erantzuna)
    return erantzuna

nk3("nitzakeen")
