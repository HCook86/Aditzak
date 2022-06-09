def subjuntivoa(aditz):
    
    nend = False

    v = aditz.verb

    if v.endswith("n"):
        nend = True
        v.removesuffix("n")