class verb:
    def __init__(self, verb):
        self.verb = verb

    teend = False

    baldintza = False
    ahalera = False
    ondorioa = False
    indikatiboa = False

aditza = str("dizkioguke")

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

def main(verb):
    if nnk(verb) != None:
        return nnk(verb)
    
    baldintza(verb)

    if not checkForKe(verb) and not verb.baldintza:
        verb.indikatiboa = True

    ahaleraORondorioa(verb)

    return verb.ahalera

print(main(verb(aditza)))
