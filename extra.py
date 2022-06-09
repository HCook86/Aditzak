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