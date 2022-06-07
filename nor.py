from json import loads

ADITZA = input("Aditza: ")

def nor(aditza):
    hand = open("nor.json", "r")
    info = hand.read()
    NOR = loads(info)

    erantzuna = False
    for element in NOR:
        tipo = NOR[element]
        for denbora in tipo:
            verbos = tipo[denbora]
            for verb in verbos.items():
                if aditza == verb[1]:
                    erantzuna = {"Aditza":aditza,"Kasua":"NOR", "Modua":element, "Denbora":denbora, "Nor":verb[0], "Nori":None, "Nork":None}
    return erantzuna
print(nor(ADITZA))
