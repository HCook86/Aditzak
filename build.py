from json import loads

#FALTA POR IMPLEMENTAR:
#   PLURAL EN EL NOR NORI NORK
#   MIRAR COMBINACIONES IMPOSIBLES
#   PREGUNTAR POR EL HIKA

#IMPLEMENTADO: 
#       NOR
#       NOR-NORI:
#           SUBJUNTIVO
#           INDIKATIVO
#           AGINTERA

def nori(args):
    verb = None
    print(args)
    if args["Nori"] == "niri":
        if args["Modua"] == "Indikatiboa":
            print("HERE")
            if args["Denbora"] == "Oraina":
                print("HERE 2")
                print(args["Aditza"])
                verb = args["Aditza"].replace("(nori)", "t")
                print(verb)
            if args["Denbora"] == "Iragana":
                verb = args["Aditza"].replace("(nori)", "da")    
        if args["Modua"] == "Subjuntiboa":
            verb = args["Aditza"].replace("(nori)", "da")
        if args["Modua"] == "Agintera":
            if args["Aditza"].endswith("te"):
                verb = args["Aditza"].replace("(nori)", "da")
            else:
                verb = args["Aditza"].replace("(nori)", "t")
        print("HALF IMPLEMENTED")
    if args["Nori"] == "hiri":
        print("NOT IMPLEMENTED")
    if args["Nori"] == "hari":
        verb = args["Aditza"].replace("(nori)", "o")
    if args["Nori"] == "guri":
        verb = args["Aditza"].replace("(nori)", "gu")
    if args["Nori"] == "zuri":
        verb = args["Aditza"].replace("(nori)", "zu")
    if args["Nori"] == "zuei":
        verb = args["Aditza"].replace("(nori)", "zue")
    if args["Nori"] == "haiei":
        if args["Modua"] == "Subjuntiboa" and args["Kasua"] == "NOR-NORI-NORK" or args["Modua"] == "Agintera" and args["Kasua"] == "NOR-NORI-NORK":
            verb = args["Aditza"].replace("(nori)", "ie")
        else:
            verb = args["Aditza"].replace("(nori)", "e")
    return verb

def nork():
    return None


def build(args):
    if args["Kasua"] == "NOR":
        handler = open("nor.json", "r")
        file = loads(handler.read())
        try:
            args["Aditza"] = file[args["Modua"]][args["Denbora"]][args["Nor"]]
        except:
            args["Aditza"] = None
            print("ERROR. NO EXISTE")
        
    if args["Kasua"] == "NOR-NORI":
        if args["Modua"] == "Indikatiboa":
            if args["Denbora"] == "Oraina":
                if args["Nor"] == "ni":
                    args["Aditza"] = "natzai"
                if args["Nor"] == "hi":
                    args["Aditza"] = "hatzai"
                if args["Nor"] == "hura":
                    args["Aditza"] = "zai"
                if args["Nor"] == "gu":
                    args["Aditza"] = "gatzaizki"
                if args["Nor"] == "zu":
                    args["Aditza"] = "zatzaizki"
                if args["Nor"] == "zuek":
                    args["Aditza"] = "zatzaizki(zuek)"
                if args["Nor"] == "haiek":
                    args["Aditza"] = "zaizki"
                
                args["Aditza"] = args["Aditza"] + ("(nori)")
            
                if args["Aditza"].startswith("zatzaizki(zuek)"):
                    args["Aditza"] = args["Aditza"].replace("(zuek)", "")
                    args["Aditza"] = args["Aditza"] + "te"

            if args["Denbora"] == "Iragana":
                if args["Nor"] == "ni":
                    args["Aditza"] = "nintzai"
                if args["Nor"] == "hi":
                    args["Aditza"] = "hintzai"
                if args["Nor"] == "hura":
                    args["Aditza"] = "zintzai"
                if args["Nor"] == "gu":
                    args["Aditza"] = "gintzaizki"
                if args["Nor"] == "zu":
                    args["Aditza"] = "zintzaizki"
                if args["Nor"] == "zuek":
                    args["Aditza"] = "zintzaizkite"
                if args["Nor"] == "haiek":
                    args["Aditza"] = "zitzaizki"
    
                args["Aditza"] = args["Aditza"] + ("(nori)") + "n"
        
        if args["Modua"] == "Subjuntiboa":
            print("SUBJUNTIVO")
            if args["Denbora"] == "Oraina":
                print("ORAINA")
                if args["Nor"] == "ni":
                    args["Aditza"] = "naki"
                if args["Nor"] == "hi":
                    args["Aditza"] = "haki"
                if args["Nor"] == "hura":
                    args["Aditza"] = "daki"
                if args["Nor"] == "gu":
                    args["Aditza"] = "gakizki"
                if args["Nor"] == "zu":
                    args["Aditza"] = "zakizki"
                if args["Nor"] == "zuek":
                    args["Aditza"] = "zakizki(zuek)"
                if args["Nor"] == "haiek":
                    args["Aditza"] = "zaizki"

                args["Aditza"] = args["Aditza"] + ("(nori)")
                

            if args["Denbora"] == "Iragana":
                print("IRAGANA")
                if args["Nor"] == "ni":
                    args["Aditza"] = "nenki"
                if args["Nor"] == "hi":
                    args["Aditza"] = "henki"
                if args["Nor"] == "hura":
                    args["Aditza"] = "leki"
                if args["Nor"] == "gu":
                    args["Aditza"] = "genkizki"
                if args["Nor"] == "zu":
                    args["Aditza"] = "zenkizki"
                if args["Nor"] == "zuek":
                    args["Aditza"] = "zenkizki(zuek)"
                if args["Nor"] == "haiek":
                    args["Aditza"] = "lekizki"

                args["Aditza"] = args["Aditza"] + ("(nori)")

            if args["Aditza"].startswith("zakizki(zuek)") or args["Aditza"].startswith("zenkizki(zuek)"):
                args["Aditza"] = args["Aditza"].replace("(zuek)", "")
                args["Aditza"] = args["Aditza"] + "te"
            args["Aditza"] = args["Aditza"] + "n"


        if args["Modua"] == "Agintera":
            print("AGINTERA")
            if args["Nor"] == "hi":
                args["Aditza"] = "haki"
            if args["Nor"] == "hura":
                args["Aditza"] = "beki"
            if args["Nor"] == "zu":
                args["Aditza"] = "zakizki"
            if args["Nor"] == "zuek":
                args["Aditza"] = "zakizki(zuek)"
            if args["Nor"] == "haiek":
                args["Aditza"] = "bekizki"

            args["Aditza"] = args["Aditza"] + ("(nori)")
            
            if args["Aditza"].startswith("zakizki(zuek)"):
                args["Aditza"] = args["Aditza"].replace("(zuek)", "")
                args["Aditza"] = args["Aditza"] + "te"

        args["Aditza"] = nori(args)
            

    if args["Kasua"] == "NOR-NORK":
        print("NOR-NORK")

    if args["Kasua"] == "NOR-NORI-NORK":
        print("NOR-NORI-NORK")
        if args["Denbora"] == "Oraina":
            if args["Denbora"] == "Oraina":
                args["Aditza"] = "di"
                #IF PLURAL PONER EL ZKI
        
        if args["Denbora"] == "Iragana":
            if args["Nork"] == "nik":
                args["Aditza"] = "ni"
            if args["Nork"] == "hik":
                args["Aditza"] = "hi"
            if args["Nork"] == "hark":
                args["Aditza"] = "zi"
            if args["Nork"] == "guk":
                args["Aditza"] = "geni"
            if args["Nork"] == "zuk":
                args["Aditza"] = "zeni"
            if args["Nork"] == "zuek":
                args["Aditza"] = "zeni(zuek)"
            if args["Nork"] == "haiek":
                args["Aditza"] = "zi(haiek)"
            

        if args["Modua"] == "Subjuntiboa":
            
            args["Aditza"] = args["Aditza"] + "eza"
            print(args["Aditza"])
            
            #IF PLURAL PONER ZKI

        args["Aditza"] = args["Aditza"] + "(nori)"

        args["Aditza"] = nori(args)

        try:
            if "(zuek)" in args["Aditza"]:
                args["Aditza"] = args["Aditza"].replace("(zuek)", "") + "te"
            if "(haiek)" in args["Aditza"]:
                args["Aditza"] = args["Aditza"].replace("(haiek)", "") + "te"
        except: pass

        """if args["Denbora"] == "Iragana":
            args["Aditza"] = args["Aditza"] + "n"
    """
    return args["Aditza"]
print(build({'Aditza': 'None', 'Kasua': 'NOR-NORI-NORK', 'Modua': 'Indikatiboa', 'Denbora': 'Oraina', 'Nor': 'zuek', 'Nori': 'niri', 'Nork': "nik"}))
