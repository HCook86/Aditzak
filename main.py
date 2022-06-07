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

aditza = str("diezazkigukegu")

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

def nnk(aditz):
    return None

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
            v = aditz.verb

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

def main(verb):
    if nnk(verb) != None:
        return nnk(verb)
    
    baldintza(verb)

    if not checkForKe(verb) and not verb.baldintza:
        verb.indikatiboa = True

    ahaleraORondorioa(verb)

    analisisCaso(verb)

    return (verb.ahalera, verb.ondorioa, verb.indikatiboa, verb.baldintza)

print(main(verb(aditza)))
