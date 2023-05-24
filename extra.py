def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

def subjuntivoa(aditz):
    
    nend = False
    ki = False

    v = aditz.verb

    if v.endswith("n"):
        nend = True
        v.removesuffix("n")

    if not v.startswith("zait"):
        v = remove_prefix(v, "za")
    v = remove_prefix(v, "zait")
    v = remove_prefix(v, "na")
    v = remove_prefix(v, "da")
    if not v.startswith("gait"):
        v = remove_prefix(v, "ga")
    v = remove_prefix(v, "de")
    v = remove_prefix(v, "gait")
    v = remove_prefix(v, "dit")

    if v.startswith("ki") or v.startswith("za") or v.startswith("dieza"):
        ki = True
    
    if ki and nend:
        v = aditz.verb

        v = remove_prefix(v, "na")
        v = remove_prefix(v, "da")
        v = remove_prefix(v, "ga")
        v = remove_prefix(v, "za")

        if v.startswith("ki"):
            aditz.ni = True
        elif v.startswith("dieza"):
            aditz.nik = True
        else:
            aditz.nk = True

        v = aditz.verb
        v = v.removesuffix("n")

        if aditz.ni:
            
            aditz.teend = False

            if v.endswith("te"):
                aditz.teend = True
                v = v.removesuffix("te")

            if v.startswith("naki"):
                aditz.nor = "ni"
            if v.startswith("daki") and not v.startswith("dakizki"):
                aditz.nor = "hura"
            if v.startswith("gakizki"):
                aditz.nor = "gu"
            if v.startswith("zakizki") and aditz.teend:
                aditz.nor = "zuek"
            elif v.startswith("zakizki"):
                aditz.nor = "zu"
            if v.startswith("dakizki"):
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
            
            if v.startswith("naza"):
                aditz.nor = "ni"
            if v.startswith("deza"):
                aditz.nor = "hura"
            if v.startswith("gaitza"):
                aditz.nor = "gu"
            if v.startswith("zaitza") and not v.startswith("zaitzate"):
                aditz.nor = "zu"
            if v.startswith("zaitzate"):
                aditz.nor = "zuek"
            if v.startswith("ditza"):
                aditz.nor = "haiek"

            if v.endswith("da"):
                aditz.nork = "nik"
            if v.endswith("za") or v.endswith("zate"):
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
            if v.endswith("da") or v.endswith("o") or v.endswith("gu") or v.endswith("zu") or v.endswith("zue") or v.endswith("e"):
                aditz.nork = "hark"
            if v.endswith("gu"):
                aditz.nork = "guk"
            if v.endswith("zu"):
                aditz.nork = "zuk"
            if v.endswith("zue"):
                aditz.nork = "zuek"
            if v.endswith("te"):
                aditz.nork = "haiek"


        kasua = None
        if aditz.nk:
            kasua = "NOR-NORK"
        elif aditz.ni:
             kasua = "NOR-NORI"
        elif aditz.nik:
            kasua = "NOR-NORI-NORK"

        modua = "Subjuntiboa"

        denbora = None
        if aditz.lehen == False:
            denbora = "Oraina"
        else:
            denbora = "Iragana"

        return {"Aditza":aditz.verb,"Kasua":kasua, "Modua":modua, "Denbora":denbora, "Nor":aditz.nor, "Nori":aditz.nori, "Nork":aditz.nork}
                
    else:
        return None

def agintera(aditz):
    
    nend = False
    ki = False

    v = aditz.verb

    if v.endswith("n"):
        nend = True

    v = remove_prefix(v, "ha")
    v = remove_prefix(v, "be")
    v = remove_prefix(v, "za")

    v = remove_prefix(v, "na")
    v = remove_prefix(v, "be")
    v = remove_prefix(v, "e")
    v = remove_prefix(v, "gait")
    v = remove_prefix(v, "bit")
    v = remove_prefix(v, "it")

    if v.startswith("ki") or v.startswith("za") or v.startswith("bieza") or v.startswith("ieza"):
        ki = True
    
    if not nend and ki:

        if v.startswith("ki"):
            aditz.ni = True
        if v.startswith("za"):
            aditz.nk = True
        if v.startswith("ieza") or v.startswith("bieza"):
            aditz.nik = True

        v = aditz.verb

        if aditz.ni:
            
            aditz.teend = False
            if v.endswith("te"):
                aditz.teend = True
                v = v.removesuffix("te")
            
            if v.startswith("haki"):
                aditz.nor = "hi"
            if v.startswith("beki") and not v.startswith("bekizki"):
                aditz.nor = "hura"
            if v.startswith("zakizki") and not aditz.teend:
                aditz.nor = "zu"
            if v.startswith("zakizki") and aditz.teend:
                aditz.nor = "zuek"
            if v.startswith("bekizki"):
                aditz.nor = "haiek"

            if v.endswith("t") or v.endswith("da"):
                aditz.nori = "niri"
            if v.endswith("k"):
                aditz.nori = "hiri"
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
            
            if v.startswith("naza"):
                aditz.nor = "ni"
            if v.startswith("beza"):
                aditz.nor = "hura"
            if v.startswith("eza"):
                aditz.nor = "hura"
            if v.startswith("gaitza"):
                aditz.nor = "gu"
            if v.startswith("bitza"):
                aditz.nor = "haiek"
            if v.startswith("itza"):
                aditz.nor = "haiek"

            if v.endswith("k"):
                aditz.nork = "hik"
            if v.endswith("zu"):
                aditz.nork = "zuk"
            if v.endswith("zue"):
                aditz.nork = "zuek"
            if v.endswith("te"):
                aditz.nork = "haiek"

        if aditz.nik:

            if v.startswith("b"):
                v = remove_prefix(v, "b")

            if v.startswith("iezazki"):
                aditz.nor = "plurala"
                v = remove_prefix(v, "iezazki")
            else:
                aditz.nor = "singularra"
                v = remove_prefix(v, "ieza")

            if v.startswith("zue"):
                aditz.nori = "zuei"
                v = remove_prefix(v, "zue")
            if v.startswith("zu"):
                aditz.nori = "zuri"
                v = remove_prefix(v, "zu")
            if v.startswith("t") or v.startswith("da"):
                aditz.nori = "niri"
                v = remove_prefix(v, "t")
                v = remove_prefix(v, "da")
            if v.startswith("k") or v.startswith("n"):
                aditz.nori = "hiri"
                v = remove_prefix(v, "k")
                v = remove_prefix(v, "n")
            if v.startswith("io") or v.startswith("o"):
                aditz.nori = "hari"
                v = remove_prefix(v, "io")
                v = remove_prefix(v, "o")
            if v.startswith("gu"):
                aditz.nori = "guri"
                v = remove_prefix(v, "gu")
            if v.startswith("ie") or v.startswith("e"):
                aditz.nori = "haiei"
                v = remove_prefix(v, "ie")
                v = remove_prefix(v, "e")

            print(v, " SIISISISI", aditz.nori)

            if v == "k":
                aditz.nork = "hik"
            if v == "":
                aditz.nork = "hark"
            if v == "zu":
                aditz.nork = "zuk"
            if v == "zue":
                aditz.nork = "zuek"
            if v == "te":
                aditz.nork = "haiek"

        kasua = None
        if aditz.nk:
            kasua = "NOR-NORK"
        elif aditz.ni:
             kasua = "NOR-NORI"
        elif aditz.nik:
            kasua = "NOR-NORI-NORK"

        modua = "Agintera"

        denbora = None
        if aditz.lehen == False:
            denbora = "Oraina"
        else:
            denbora = "Iragana"

        return {"Aditza":aditz.verb,"Kasua":kasua, "Modua":modua, "Denbora":denbora, "Nor":aditz.nor, "Nori":aditz.nori, "Nork":aditz.nork}
                
    else:
        return None
