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

    v = remove_prefix(v, "na")
    v = remove_prefix(v, "da")
    v = remove_prefix(v, "ga")
    v = remove_prefix(v, "za")
    v = remove_prefix(v, "de")
    v = remove_prefix(v, "gait")
    v = remove_prefix(v, "zait")
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
            pass

        if aditz.nik:
            pass


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