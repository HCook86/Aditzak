from app import remove_prefix

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
        v.removesuffix("n")

        print("esubjuntivo")