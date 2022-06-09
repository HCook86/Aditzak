from json import loads

class verb:
    def __init__(self, verb):
        self.verb = verb

    teend = False

    baldintza = False
    ahalera = False
    ondorioa = False
    indikatiboa = False

    nk = False
    ni = False
    nik = False
    lehen = False

    nor = None
    nori = None
    nork = None

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

def nor(aditz):
    
    hand = open("nor.json", "r")
    info = hand.read()
    NOR = loads(info)

    erantzuna = None
    for element in NOR:
        tipo = NOR[element]
        for denbora in tipo:
            verbos = tipo[denbora]
            for verb in verbos.items():
                if aditz.verb == verb[1]:
                    erantzuna = {"Aditza":aditz.verb,"Kasua":"NOR", "Modua":element, "Denbora":denbora, "Nor":verb[0], "Nori":None, "Nork":None}
                    break
    return erantzuna

def nornork(aditz):
    hand = open("nk3.json", "r")
    info = hand.read()
    NK3 = loads(info)
    
    erantzuna = None
    for element in NK3:
        tipo = NK3[element]
        for zenbaki in tipo:
            verbos = tipo[zenbaki]
            for tiempo in verbos:
                pertsonak = verbos[tiempo]
                for pertsona in pertsonak.items():
                    if aditz.verb == pertsona[1]:
                        sujeto = None
                        if tiempo == "Singularra":
                            sujeto = "hura"
                        elif tiempo == "Plurala":
                            sujeto = "haiek"
                        erantzuna = {"Aditza":aditz.verb,"Kasua":"NOR-NORK", "Modua":element, "Denbora":zenbaki, "Nor":sujeto, "Nori":None, "Nork":pertsona[0]}
    return erantzuna

def baldintza(aditz):
    if aditz.verb[:2] == "ba":
        aditz.baldintza = True

def checkForKe(aditz):
    v = aditz.verb

    if v[-2:] == "ke":
        return True

    if v[-3:] in {"t", "o", "gu", "zu", "zue", "e", "da"} or v[-2:] in {"t", "o", "gu", "zu", "zue", "e", "da"} or v[-1:] in {"t", "o", "gu", "zu", "zue", "e", "da"}:

        v = v.removesuffix('e')
        v = v.removesuffix('t')
        v = v.removesuffix('o')
        v = v.removesuffix('gu')
        v = v.removesuffix('zu')
        v = v.removesuffix('zue')
        v = v.removesuffix('da')

    if v[-2:] == "te":
        aditz.teend = True
        v = v[:-2]

    if v[-2:] == "ke":
        return True

    return False

def ahaleraORondorioa(aditz):
    if checkForKe(aditz):
        fl = aditz.verb[:5]
        
        if fl == "dieza":
            aditz.ahalera = True
        else:
            tl = aditz.verb[:2]
            if tl in {"na", "da", "ga", "za", "de", "di"}:
                aditz.ahalera = True
            else:
                aditz.ondorioa = True

def analisisCaso(aditz):

    v = aditz.verb
    if aditz.indikatiboa == True:

        v = remove_prefix(v, "na")
        v = remove_prefix(v, "d")
        v = remove_prefix(v, "gait")
        v = remove_prefix(v, "zait")
        v = remove_prefix(v, "dit")
        v = remove_prefix(v, "nind")
        v = remove_prefix(v, "gint")
        v = remove_prefix(v, "zint")

        if v[:1] == "u":
            aditz.nk = True
        else:
            v = aditz.verb

            v = remove_prefix(v, "nat")
            v = remove_prefix(v, "gat")
            v = remove_prefix(v, "zat")
            v = remove_prefix(v, "nint")
            v = remove_prefix(v, "zit")
            v = remove_prefix(v, "gint")
            v = remove_prefix(v, "zint")

            if v[:3] == "zai":
                aditz.ni = True
            else:
                aditz.nik = True

    if aditz.baldintza == True:

        v = remove_prefix(v, "ba")

        v = remove_prefix(v, "nint")
        v = remove_prefix(v, "lit")
        v = remove_prefix(v, "gint")
        v = remove_prefix(v, "zint")

        if v[:3] == "zai":
            aditz.ni = True
        else: 
            v = aditz.verb

            v = remove_prefix(v, "ba")

            v = remove_prefix(v, "nind")
            v = remove_prefix(v, "gint")
            v = remove_prefix(v, "zint")

            if v[:1] == "u":
                aditz.nk = True
            else:
                aditz.nik = True

    if aditz.ondorioa == True:

        v = remove_prefix(v, "nint")
        v = remove_prefix(v, "lit")
        v = remove_prefix(v, "gint")
        v = remove_prefix(v, "zint")

        if v[:3] == "zai":
            aditz.ni = True
        else: 
            v = aditz.verb

            v = remove_prefix(v, "nind")
            v = remove_prefix(v, "gint")
            v = remove_prefix(v, "zint")

            if v[:1] == "u":
                aditz.nk = True
            else:
                aditz.nik = True

    if aditz.ahalera == True:
        
        v = remove_prefix(v, "na")
        v = remove_prefix(v, "da")
        v = remove_prefix(v, "ga")
        v = remove_prefix(v, "za")

        if v[:2] == "ki":
            aditz.ni = True
        else:
            v = aditz.verb

            if v[:5] == "dieza":
                aditz.nik = True
            else:
                aditz.nk = True

def indikativoPersonas(aditz):
    if aditz.indikatiboa:
        
        v = aditz.verb
        if aditz.ni:

            if v[-1] == "n":
                aditz.lehen = True

            if v.startswith("na") or  v.startswith("nin"):
                aditz.nor =  "ni"
            if v.startswith("ga") or  v.startswith("gin"):
                aditz.nor =  "gu"
            
            aditz.teend = False

            if v.endswith("te"):
                aditz.teend = True
            else:
                v = v.removesuffix("dan")
                v = v.removesuffix("on")
                v = v.removesuffix("gun")
                v = v.removesuffix("zun")
                v = v.removesuffix("zuen")
                v = v.removesuffix("en")

                if v.endswith("te"):
                    aditz.teend = True
            
            if (v.startswith("za") and not aditz.teend) or  (v.startswith("zin") and not aditz.teend):
                aditz.nor =  "zu"

            if (v.startswith("za") and aditz.teend) or  (v.startswith("zin") and aditz.teend):
                aditz.nor =  "zuek"

            if v.startswith("zaizki") or v.startswith("zitzaizki"):
                aditz.nor = "haiek"

            elif v.startswith("zai") or  v.startswith("zit"):
                aditz.nor =  "hura"

            v = aditz.verb
            v = v.removesuffix("te")
            v = v.removesuffix("n")

            if v.endswith("t") or  v.endswith("da"):
                aditz.nori =  "niri"
            if v.endswith("o"):
                aditz.nori =  "hari"
            if v.endswith("gu"):
                aditz.nori =  "guri"
            if v.endswith("zu"):
                aditz.nori =  "zuri"
            if v.endswith("zue"):
                aditz.nori =  "zuei"
            if v.endswith("e") and not v.endswith("zue"):
                aditz.nori =  "haiei"

        if aditz.nk:
            
            if v.endswith("n"):
                aditz.lehen = True

            if v.startswith("nau") or v.startswith("nindu"):
                aditz.nor = "ni"
            if v.startswith("du"):
                aditz.nor = "hura"
            if v.startswith("gaitu") or v.startswith("gintu"):
                aditz.nor = "gu"
            if v.startswith("zaituzte") or v.startswith("zintuzte"):
                aditz.nor = "zuek"
            elif v.startswith("zaitu") or v.startswith("zintu"): 
                aditz.nor = "zu"
            if v.startswith("ditu"):
                aditz.nor = "haiek"
            
            if v.endswith("t") or v.endswith("dan"):
                aditz.nork = "nik"
            if v.endswith("u") or v.endswith("en"):
                aditz.nork = "hark"
            if v.endswith("gu") or v.endswith("gun"):
                aditz.nork = "guk"
            if v.endswith("zu") or v.endswith("zun"):
                aditz.nork = "zuk"
            if v.endswith("zue") or v.endswith("zuen"):
                aditz.nork = "zuek"
            if v.endswith("te") or v.endswith("ten"):
                aditz.nork = "haiek"

        if aditz.nik:
            
            if v.endswith("n"):
                aditz.lehen = True

            if aditz.lehen == False:

                if v.startswith("dizki"):
                    aditz.nor = "plu"
                    v = remove_prefix(v, "dizki")
                else:
                    aditz.nor = "sin"
                    v = remove_prefix(v, "di")

                if v.startswith("t") or v.startswith("da"):
                    aditz.nori = "niri"
                if v.startswith("o"):
                    aditz.nori = "hari"
                if v.startswith("gu"):
                    aditz.nori = "guri"
                if v.startswith("zu"):
                    aditz.nori = "zuri"
                if v.startswith("zue"):
                    aditz.nori = "zuei"
                if v.startswith("e"):
                    aditz.nori = "haiei"

                if v.endswith("t"):
                    aditz.nork = "nik"
                elif v.endswith("gu"):
                    aditz.nork = "guk"
                elif v.endswith("zu"):
                    aditz.nork = "zuk"
                elif v.endswith("zue"):
                    aditz.nork = "zuek"
                elif v.endswith("te"):
                    aditz.nork = "haiek"
                else:
                    aditz.nork = "hark"    
            
            else:
                v = v.removesuffix("n")

                aditz.teend = False

                if v.endswith("te"):
                    aditz.teend = True
                    v = v.removesuffix("te") 
                if v.startswith("n"):
                    aditz.nork = "nik"
                    v = remove_prefix(v, "n")
                if v.startswith("z") and aditz.teend and not v.startswith("zen"):
                    aditz.nork = "haiek"
                    v = remove_prefix(v, "z")
                elif v.startswith("z") and not v.startswith("zen"):
                    aditz.nork = "hark"
                    v = remove_prefix(v, "z")
                if v.startswith("gen"):
                    aditz.nork = "guk"
                    v = remove_prefix(v, "gen")
                if v.startswith("zen") and aditz.teend:
                    aditz.nork = "zuek"
                    v = remove_prefix(v, "zen")
                elif v.startswith("zen"):
                    aditz.nork("zuk")
                    v = remove_prefix(v, "zen")
                if v.startswith("izki"):
                    aditz.nor = "plu"
                    v = remove_prefix(v, "izki")
                else:
                    aditz.nor = "sin"
                    v = remove_prefix(v, "i")

                if v == "da":
                    aditz.nori = "niri"
                if v == "o":
                    aditz.nori = "hari"
                if v == "gu":
                    aditz.nori = "guri"
                if v == "zu":
                    aditz.nori = "zuri"
                if v == "zue":
                    aditz.nori = "zuei"
                if v == "e":
                    aditz.nori = "haiei"

def baldintzaPersonas(aditz):
    if aditz.baldintza:

        v = aditz.verb
        v = remove_prefix(v, "ba")
        if aditz.ni:
            
            aditz.teend = False

            if v.endswith("te"):
                aditz.teend = True
                v = v.removesuffix("te")

            if v.startswith("nintzai"):
                aditz.nor = "ni"
            if v.startswith("litzaizki"):
                aditz.nor = "haiek"
            elif v.startswith("litzai"):
                aditz.nor = "hura"
            if v.startswith("gintzaizki"):
                aditz.nor = "gu"
            if v.startswith("zintzaizki") and aditz.teend:
                aditz.nor = "zuek"
            if v.startswith("zintzaizki") and not aditz.teend:
                aditz.nor = "zu"

            if v.endswith("t") or v.endswith("da"):
                aditz.nori = "niri"
            if v.endswith("o"):
                aditz.nori = "hari"
            if v.endswith("gu"):
                aditz.nori = "guri"
            if v.endswith("zu"):
                aditz.nori = "zuri"
            if v.endswith("zue"):
                aditz.nori = "zuei"
            if v.endswith("e") and not v.endswith("zue"):
                aditz.nori = "haiei"
        
        if aditz.nk:
            
            aditz.teend = False

            v = v.removesuffix("tet")
            v = v.removesuffix("tegu")
            v = v.removesuffix("tezu")
            v = v.removesuffix("tezue")
            v = v.removesuffix("tete")

            if v.endswith("z") or v.endswith("zte"):
                aditz.teend = True
            
            if not v.endswith("zte"):
                v = aditz.verb
                v = remove_prefix(v, "ba")
            else:
                v = v.removesuffix("zte")

            if v.startswith("nindu"):
                aditz.nor = "ni"
            if v.startswith("gintu"):
                aditz.nor = "gu"
            if v.startswith("zintu") and aditz.teend:
                aditz.nor = "zuek"
            elif v.startswith("zintu"):
                aditz.nor = "zu"

            if v.endswith("t"):
                aditz.nork = "nik"
            if v.endswith("u") and not v.endswith("gu") and not v.endswith("zu"):
                aditz.nork = "hark"
            if v.endswith("gu"):
                aditz.nork = "guk"
            if v.endswith("zu"):
                aditz.nork = "zuk"
            if v.endswith("zue"):
                aditz.nork = "zuek"
            if v.endswith("te"):
                aditz.nork = "haiek"
        
        if aditz.nik:
            
            aditz.teend = False

            if v.endswith("te"):
                aditz.teend = True
                v = v.removesuffix("te")

            if v.startswith("n"):
                aditz.nork = "nik"
                v = remove_prefix(v, "n")
            if v.startswith("gen"):
                aditz.nork = "guk"
                v = remove_prefix(v, "gen")
            if v.startswith("l") and aditz.teend:
                aditz.nork = "haiek"
                v = remove_prefix(v, "l")
            elif v.startswith("l"):
                aditz.nork = "hark"
                v = remove_prefix(v, "l")
            if v.startswith("zen") and aditz.teend:
                aditz.nork = "zuek"
                v = remove_prefix(v, "zen")
            elif v.startswith("zen"):
                aditz.nork = "zuk"
                v = remove_prefix(v, "zen")

            if v.startswith("izki"):
                aditz.nor = "plu"
                v = remove_prefix(v, "izki")
            else:
                aditz.nor = "sin"
                v = remove_prefix(v, "i")

            if v == "t" or v == "da":
                aditz.nori = "niri"
            if v == "o":
                aditz.nori = "hari"
            if v == "gu":
                aditz.nori = "guri"
            if v == "zu":
                aditz.nori = "zuri"
            if v == "zue":
                aditz.nori = "zuei"
            if v == "e":
                aditz.nori = "haiei"

def ahaleraPersonas(aditz):
    if aditz.ahalera:
        
        v = aditz.verb
        if aditz.ni:
            
            aditz.teend = False

            if v.endswith("te"):
                aditz.teend = True
                v = v.removesuffix("te")

            if v.startswith("naki"):
                aditz.nor = "ni"
            if v.startswith("gakizki"):
                aditz.nor = "gu"
            if v.startswith("daki") and not v.startswith("dakizki"):
                aditz.nor = "hura"
            if v.startswith("dakizki"):
                aditz.nor = "haiek"
            if v.startswith("zakizki") and aditz.teend:
                aditz.nor = "zuek"
            elif v.startswith("zakizki"):
                aditz.nor = "zu"

            if v.endswith("dake"):
                aditz.nori = "niri"
            if v.endswith("oke"):
                aditz.nori = "hari"
            if v.endswith("guke"):
                aditz.nori = "guri"
            if v.endswith("zuke"):
                aditz.nori = "zuri"
            if v.endswith("zueke"):
                aditz.nori = "zuei"
            if v.endswith("eke") and not v.endswith("zueke"):
                aditz.nori = "haiei"

        if aditz.nk:

            if v.startswith("nazake"):
                aditz.nor = "ni"
            if v.startswith("dezake"):
                aditz.nor = "hura"
            if v.startswith("gaitzake"):
                aditz.nor = "gu"
            if v.startswith("zaitzake") and not v.startswith("zaitzakete"):
                aditz.nor = "zu"
            if v.startswith("zaitzakete"):
                aditz.nor = "zuek"
            if v.startswith("ditzake"):
                aditz.nor = "haiek"

            if v.endswith("t"):
                aditz.nork = "nik"
            if v.endswith("zake") or v.endswith("zakete"):
                aditz.nork = "hark"
            if v.endswith("gu"):
                aditz.nork = "guk"
            if v.endswith("zu"):
                aditz.nork = "zuk"
            if v.endswith("zue"):
                aditz.nork = "zuek"
            if v.endswith("te"):
                aditz.nork = "haiek"

        if aditz.nik:
            
            if v.startswith("diezazki"):
                aditz.nor = "plu"
                v = remove_prefix(v, "diezazki")
            else:
                aditz.nor = "sin"
                v = remove_prefix(v, "dieza")

            if v.startswith("da"):
                aditz.nori = "niri"
            if v.startswith("io") or v.startswith("o"):
                aditz.nori = "hari"
            if v.startswith("gu"):
                aditz.nori = "guri"
            if v.startswith("zu"):
                aditz.nori = "zuri"
            if v.startswith("zue"):
                aditz.nori = "zuei"
            if v.startswith("e") or v.startswith("ie"):
                aditz.nori = "haiei"

            if v.endswith("t"):
                aditz.nork = "nik"
            if v.endswith("ke"):
                aditz.nork = "hark"
            if v.endswith("gu"):
                aditz.nork = "guk"
            if v.endswith("zu"):
                aditz.nork = "zuk"
            if v.endswith("zue"):
                aditz.nork = "zuek"
            if v.endswith("te"):
                aditz.nork = "haiek"

def ondorioaPersonas(aditz):
    
    if aditz.ondorioa:

        v = aditz.verb
        if aditz.ni:
            
            aditz.teend = False

            if v.endswith("te"):
                aditz.teend = True
                v = v.removesuffix("te")

            v = v.removesuffix("ke")

            if v.startswith("nin"):
                aditz.nor = "ni"
            if v.startswith("litzai") and not v.startswith("litzaizki"):
                aditz.nor = "hura"
            if v.startswith("gin"):
                aditz.nor = "gu"
            if v.startswith("zin") and aditz.teend:
                aditz.nor = "zuek"
            elif v.startswith("zin"):
                aditz.nor = "zu"
            if v.startswith("litzaizki"):
                aditz.nor = "haiek"

            if v.endswith("da"):
                aditz.nori = "niri"
            if v.endswith("o"):
                aditz.nori = "hari"
            if v.endswith("gu"):
                aditz.nori = "guri"
            if v.endswith("zu"):
                aditz.nori = "zuri"
            if v.endswith("zue"):
                aditz.nori = "zuei"
            if v.endswith("e") and not v.endswith("zue"):
                aditz.nori = "haiei"

        if aditz.nk:
            
            if v.startswith("nindu"):
                aditz.nor = "ni"
            if v.startswith("gintu"):
                aditz.nor = "gu"
            if v.startswith("zintu") and not v.startswith("zintuzte"):
                aditz.nor = "zu"
            if v.startswith("zintuzte"):
                aditz.nor = "zuek"

            if v.endswith("t"):
                aditz.nork = "nik"
            if v.endswith("ke"):
                aditz.nork = "hark"
            if v.endswith("gu"):
                aditz.nork = "guk"
            if v.endswith("zu"):
                aditz.nork = "zuk"
            if v.endswith("zue"):
                aditz.nork = "zuek"
            if v.endswith("te"):
                aditz.nork = "haiek"

        if aditz.nik:
            
            aditz.teend = False

            if v.endswith("te"):
                aditz.teend = True
                v = v.removesuffix("te")

            if v.startswith("n"):
                aditz.nork = "nik"
                v = remove_prefix(v, "n")
            if v.startswith("l") and aditz.teend:
                aditz.nork = "haiek"
                v = remove_prefix(v, "l")
            elif v.startswith("l"):
                aditz.nork = "hark"
                v = remove_prefix(v, "l")
            if v.startswith("gen"):
                aditz.nork = "guk"
                v = remove_prefix(v, "gen")
            if v.startswith("zen") and aditz.teend:
                aditz.nork = "zuek"
                v = remove_prefix(v, "zen")
            elif v.startswith("zen"):
                aditz.nork = "zuk"
                v = remove_prefix(v, "zen")

            if v.startswith("izki"):
                aditz.nor = "plu"
                v = remove_prefix(v, "izki")
            else:
                aditz.nor = "sin"
                v = remove_prefix(v, "i")

            if v == "dake":
                aditz.nori = "niri"
            if v == "oke":
                aditz.nori = "hari"
            if v == "guke":
                aditz.nori = "guri"
            if v == "zuke":
                aditz.nori = "zuri"
            if v == "zueke":
                aditz.nori = "zuei"
            if v == "eke":
                aditz.nori = "haiei"

def main(verb):

    if nor(verb) != None:
        return nor(verb)

    if nornork(verb) != None:
        return nornork(verb)
    
    baldintza(verb)

    if not checkForKe(verb) and not verb.baldintza:
        verb.indikatiboa = True

    ahaleraORondorioa(verb)

    analisisCaso(verb)

    indikativoPersonas(verb)

    baldintzaPersonas(verb)

    ahaleraPersonas(verb)

    ondorioaPersonas(verb)

    kasua = None
    if verb.nk:
        kasua = "NOR-NORK"
    elif verb.ni:
        kasua = "NOR-NORI"
    elif verb.nik:
        kasua = "NOR-NORI-NORK"

    modua = None
    if verb.indikatiboa:
        modua = "Indikatiboa"
    elif verb.baldintza:
        modua = "Baldintza"
    elif verb.ahalera:
        modua = "Ahalera"
    elif verb.ondorioa:
        modua = "Ondorioa"

    denbora = None
    if verb.lehen == False:
        denbora = "Oraina"
    else:
        denbora = "Iragana"

    return {"Aditza":verb.verb,"Kasua":kasua, "Modua":modua, "Denbora":denbora, "Nor":verb.nor, "Nori":verb.nori, "Nork":verb.nork}

def analyse(aditz):
        return main(verb(aditz.lower()))
