from json import loads

#FALTA POR IMPLEMENTAR:
#   NOR-NORI-NORK EN AGINTERA COMBINACIONES IMPOSIBLES
#   MIRAR COMBINACIONES IMPOSIBLES
#   PREGUNTAR POR EL HIKA

#IMPLEMENTADO: 
#       NOR
#       NOR-NORI: (TODO MENOS AHALERA)
#           SUBJUNTIVO
#           INDICATIVO
#           AGINTERA
#           BALDINTZA
#           ONDORIOA
#           
#       NOR-NORI-NORK: (TODO MENOS AHALERA) (EL AGINTERA NO RECONOCE COMBINACIONES IMPOSIBLES)
#           SUBJUNTIVO
#           INDICATIVO
#           AGINTERA
#           BALDINTZA
#           ONDORIOA
#
#       NOR-NORK
#           INDICATIVO (PRESENTE)
#           3 PERSONA DEL ARCHIVO nk3.json (MENOS ONDORIOA, QUE NO ESTÁ IMPLEMENTADO)

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
        if args["Modua"] == "Agintera" and args["Aditza"].endswith("i(nori)") == False:
            verb = args["Aditza"].replace("(nori)", "io")
        else:
            verb = args["Aditza"].replace("(nori)", "o")
    if args["Nori"] == "guri":
        verb = args["Aditza"].replace("(nori)", "gu")
    if args["Nori"] == "zuri":
        verb = args["Aditza"].replace("(nori)", "zu")
    if args["Nori"] == "zuei":
        verb = args["Aditza"].replace("(nori)", "zue")
    if args["Nori"] == "haiei":
        if args["Modua"] == "Subjuntiboa" and args["Kasua"] == "NOR-NORI-NORK" or args["Modua"] == "Agintera":
            verb = args["Aditza"].replace("(nori)", "ie")
        else:
            verb = args["Aditza"].replace("(nori)", "e")
    return verb

def nork(args):
    verb = None
    print(args)
    if args["Nork"] == "nik":
        verb = args["Aditza"].replace("(nork)", "t")
    """if args["Nork"] == "hik":
    """
    if args["Nork"] == "hark":
        verb = args["Aditza"].replace("(nork)", "")
        print("(NOTHING)")
    if args["Nork"] == "guk":
        verb = args["Aditza"].replace("(nork)", "gu")
        print("gu")
    if args["Nork"] == "zuk":
        verb = args["Aditza"].replace("(nork)", "zu")
        print("zu")
    if args["Nork"] == "zuek":
        verb = args["Aditza"].replace("(nork)", "zue")
        print("zue")
    if args["Nork"] == "haiek":
        verb = args["Aditza"].replace("(nork)", "e")
        print("e")
    return verb


def build(args):
    #If Aditza isn't None, raie an exception
    if args["Aditza"] != None:
        raise ValueError('Incorrect value for Aditza: Aditza always must have the value None. Read README.txt or the documentation at https://github.com/HCook86/Aditzak/blob/heroku/README.md for more information')
    if args["Kasua"] == "NOR":
        handler = open("nor.json", "r")
        file = loads(handler.read())
        try:
            args["Aditza"] = file[args["Modua"]][args["Denbora"]][args["Nor"]]
        except:
            args["Aditza"] = None
            print("ERROR. NO EXISTE")

    #If the case is NOR-NORI  
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
        
        if args["Modua"] == "Baldintza":
            args["Aditza"] = "ba"
            
            if args["Nor"] == "ni":
                args["Aditza"] = args["Aditza"] + "nintzai"
            if args["Nor"] == "hi":
                args["Aditza"] = args["Aditza"] + "hintzai"
            if args["Nor"] == "hura":
                args["Aditza"] = args["Aditza"] + "litzai"
            if args["Nor"] == "gu":
                args["Aditza"] = args["Aditza"] +  "gintzaizki"
            if args["Nor"] == "zu":
                args["Aditza"] = args["Aditza"] +  "zintzaizki"
            if args["Nor"] == "zuek":
                args["Aditza"] = args["Aditza"] +  "zintzaizki(zuek)"
            if args["Nor"] == "haiek":
                args["Aditza"] = args["Aditza"] +  "litzaizki"

            args["Aditza"] = args["Aditza"] + ("(nori)")

            if args["Aditza"].startswith("bazintzaizki(zuek)"):
                args["Aditza"] = args["Aditza"].replace("(zuek)", "")
                args["Aditza"] = args["Aditza"] + "te"

        if args["Modua"] == "Ondorioa":
            print("ONDORIOA")
            if args["Nor"] == "ni":
                args["Aditza"] = "nintzai"
            if args["Nor"] == "hi":
                args["Aditza"] = "hintzai"
            if args["Nor"] == "hura":
                args["Aditza"] = "litzai"
            if args["Nor"] == "gu":
                args["Aditza"] = "gintzaizki"
            if args["Nor"] == "zu":
                args["Aditza"] = "zintzaizki"
            if args["Nor"] == "zuek":
                args["Aditza"] = "zintzaizki(zuek)"
            if args["Nor"] == "haiek":
                args["Aditza"] = "litzaizki"

            args["Aditza"] = args["Aditza"] + ("(nori)")

            args["Aditza"] = args["Aditza"] + "ke"
            
            if args["Aditza"].startswith("zintzaizki(zuek)"):
                args["Aditza"] = args["Aditza"].replace("(zuek)", "")
                args["Aditza"] = args["Aditza"] + "te"

            if args["Denbora"] == "Iragana":
                if args["Aditza"].endswith("te"):
                    args["Aditza"] = args["Aditza"] + "n"
                else:
                    args["Aditza"] = args["Aditza"] + "en"

        if args["Modua"] == "Ahalera":
            print("AHALERA")
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

            args["Aditza"] = args["Aditza"] + "ke"

            if args["Aditza"].startswith("zakizki(zuek)"):
                args["Aditza"] = args["Aditza"].replace("(zuek)", "")
                args["Aditza"] = args["Aditza"] + "te"


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
        handler = open("nk3.json", "r")
        file = loads(handler.read())
        try:
            if args["Nor"] == "hura":
                Denbora = "Singularra"
            if args["Nor"] == "haiek":
                Denbora = "Plurala"
            args["Aditza"] = file[args["Modua"]][args["Denbora"]][Denbora][args["Nork"]]
            return args["Aditza"]
        except:
            args["Aditza"] = None
            print("ERROR. NO EXISTE")
            
        if args["Denbora"] == "Oraina":
            if args["Nor"] == "ni":
                args["Aditza"] = "na"
            if args["Nor"] == "hi":
                args["Aditza"] = "ha"
            if args["Nor"] == "hura":
                args["Aditza"] = "d"
            if args["Nor"] == "gu":
                args["Aditza"] = "gait"    
            if args["Nor"] == "zu":
                args["Aditza"] = "zait"
            if args["Nor"] == "zuek":
                args["Aditza"] = "zait(zuek)"
            if args["Nor"] == "haiek":
                args["Aditza"] = "dit"
        
        if args["Modua"] == "Indikatiboa":
            args["Aditza"] = args["Aditza"] + "u"
        if args["Modua"] == "Subjuntiboa":
            args["Aditza"] = args["Aditza"] + "za"

        has_zte = ["Indikatiboa", "Ahalera", "baldintza"]
        if "(zuek)" in args["Aditza"] and args["Modua"] in has_zte:
            args["Aditza"] = args["Aditza"].replace("(zuek)", "") + "zte"
        else: 
            args["Aditza"] = args["Aditza"].replace("(zuek)", "") + "te"

        args["Aditza"] = args["Aditza"] + "(nork)"
        args["Aditza"] = nork(args)

        if args["Modua"] == "Subjuntiboa":    
            args["Aditza"] = args["Aditza"] + "n"

    if args["Kasua"] == "NOR-NORI-NORK":
        print("NOR-NORI-NORK")
        print(args["Nor"])
        args["Aditza"] = ""
        if args["Nor"] != "singularra" and args["Nor"] != "plurala":
            raise ValueError("Incorrect value for Nor: Nor only takes singularra or plurala when Kasua is NOR-NORI-NORK. Read README.txt or the documentation at https://github.com/HCook86/Aditzak/blob/heroku/README.md for more information")
        if args["Modua"] == "Baldintza":
            if args["Denbora"] != "Oraina":
                raise ValueError("Incorrect value for Denbora: Denbora only takes Oraina when Modua is Baldintza. Read README.txt or the documentation at https://github.com/HCook86/Aditzak/blob/heroku/README.md for more information")
            args["Aditza"] = "ba"
        if args["Modua"] == "Agintera":
            args["Aditza"] = "ieza"
        else:
            if args["Denbora"] == "Oraina" and args["Modua"] != "Baldintza" and args["Modua"] != "Ondorioa":
                args["Aditza"] = "di"
        
        if args["Denbora"] == "Iragana" or args["Modua"] == "Baldintza" or args["Modua"] == "Ondorioa":
            if args["Nork"] == "nik":
                args["Aditza"] = args["Aditza"] + "ni"
            if args["Nork"] == "hik":
                args["Aditza"] = args["Aditza"] + "hi"
            if args["Nork"] == "hark":
                args["Aditza"] = args["Aditza"] + "zi"
            if args["Nork"] == "guk":
                args["Aditza"] = args["Aditza"] + "geni"
            if args["Nork"] == "zuk":
                args["Aditza"] = args["Aditza"] + "zeni"
            if args["Nork"] == "zuek":
                args["Aditza"] = args["Aditza"] + "zeni(zuek)"
            if args["Nork"] == "haiek":
                args["Aditza"] = args["Aditza"] + "zi(haiek)"
        


        if args["Modua"] == "Subjuntiboa":
            
            args["Aditza"] = args["Aditza"] + "eza"
            print(args["Aditza"])
            
            if args["Nor"] == "plurala":
                args["Aditza"] = args["Aditza"] + "zki"
        else:
            if args["Nor"] == "plurala":
                args["Aditza"] = args["Aditza"] + "zki" 
        args["Aditza"] = args["Aditza"] + "(nori)"

        args["Aditza"] = nori(args)
        print("AFTER NORI " + args["Aditza"])
        if args["Denbora"] == "Oraina" and args["Modua"] != "Baldintza" and args["Modua"] != "Ondorioa":
            args["Aditza"] = args["Aditza"] + "(nork)"
            args["Aditza"] = nork(args)

        if args["Modua"] == "Ondorioa":
            args["Aditza"] = args["Aditza"] + "ke"

        try:
            if "(zuek)" in args["Aditza"]:
                args["Aditza"] = args["Aditza"].replace("(zuek)", "") + "te"
            if "(haiek)" in args["Aditza"]:
                args["Aditza"] = args["Aditza"].replace("(haiek)", "") + "te"
        except: pass

        if args["Denbora"] == "Iragana" or args["Modua"] == "Subjuntiboa":
            if args["Modua"] == "Ondorioa" and args["Aditza"].endswith("te") == False:
                args["Aditza"] = args["Aditza"] + "en"
            else:    
                args["Aditza"] = args["Aditza"] + "n"
    
    #If Kasua does not have a correct value
    else: raise ValueError('Incorrect value for Kasua. Read README.txt or the documentation at https://github.com/HCook86/Aditzak/blob/heroku/README.md for more information')
    return args["Aditza"]
print(build({'Aditza': None, 'Kasua': 'NOR-NORK', 'Modua': 'Baldintza', 'Denbora': "Oraina", 'Nor': 'hura', 'Nori': 'hari', 'Nork': "guk"}))
