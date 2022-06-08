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
            for verb in verbos.items():
                if aditza == verb[1]:
                    erantzuna = {"Aditza":aditza,"Kasua":"NOR-NORK", "Modua":element, "Denbora":denbora, "Nor":"", "Nori":None, "Nork":verb[0]}
    return erantzuna
