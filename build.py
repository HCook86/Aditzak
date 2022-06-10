from json import loads

#MIRAR COMBINACIONES IMPOSIBLES
#PREGUNTAR POR EL HIKA

def build(args):
    if args["Kasua"] == "NOR":
        handler = open("nor.json", "r")
        file = loads(handler.read())
        try:
            aditza = file[args["Modua"]][args["Denbora"]][args["Nor"]]
        except:
            aditza = None
            print("ERROR. NO EXISTE")
        

    if args["Kasua"] == "NOR-NORI":
        aditza = str()
        if args["Modua"] == "Indikatiboa":
            if args["Denbora"] == "Oraina":
                if args["Nor"] == "ni":
                    aditza = "natzai"
                if args["Nor"] == "hi":
                    aditza = "hatzai"
                if args["Nor"] == "hura":
                    aditza = "zai"
                if args["Nor"] == "gu":
                    aditza = "gatzaizki"
                if args["Nor"] == "zu":
                    aditza = "zatzaizki"
                if args["Nor"] == "zuek":
                    aditza = "zatzaizki(zuek)"
                if args["Nor"] == "haiek":
                    aditza = "zaizki"
                

                if args["Nori"] == "niri":
                        aditza = aditza + "t"
                #PREGUNTAR
                """if args["Nori"] == "hiri":
                    aditza = aditza + """
                if args["Nori"] == "hari":
                    aditza = aditza + "o"
                if args["Nori"] == "guri":
                    aditza = aditza + "gu"
                if args["Nori"] == "zuri":
                    aditza = aditza + "zu"
                if args["Nori"] == "zuei":
                    aditza = aditza + "zue"
                if args["Nori"] == "haiei":
                    aditza = aditza + "e"
            
                if aditza.startswith("zatzaizki(zuek)"):
                    aditza = aditza.replace("(zuek)", "")
                    aditza = aditza + "te"

            if args["Denbora"] == "Iragana":
                if args["Nor"] == "ni":
                    aditza = "nintzai"
                if args["Nor"] == "hi":
                    aditza = "hintzai"
                if args["Nor"] == "hura":
                    aditza = "zintzai"
                if args["Nor"] == "gu":
                    aditza = "gintzaizki"
                if args["Nor"] == "zu":
                    aditza = "zintzaizki"
                if args["Nor"] == "zuek":
                    aditza = "zintzaizkite"
                if args["Nor"] == "haiek":
                    aditza = "zitzaizki"
    

                if args["Nori"] == "niri":
                        aditza = aditza + "da"
                #PREGUNTAR
                """if args["Nori"] == "hiri":
                    aditza = aditza + """
                if args["Nori"] == "hari":
                    aditza = aditza + "o"
                if args["Nori"] == "guri":
                    aditza = aditza + "gu"
                if args["Nori"] == "zuri":
                    aditza = aditza + "zu"
                if args["Nori"] == "zuei":
                    aditza = aditza + "zue"
                if args["Nori"] == "haiei":
                    aditza = aditza + "e"

                aditza = aditza + "n"
        
        if args["Modua"] == "Subjuntiboa":
            print("SUBJUNTIVO")
            if args["Denbora"] == "Oraina":
                print("ORAINA")
                if args["Nor"] == "ni":
                    aditza = "naki"
                if args["Nor"] == "hi":
                    aditza = "haki"
                if args["Nor"] == "hura":
                    aditza = "daki"
                if args["Nor"] == "gu":
                    aditza = "gakizki"
                if args["Nor"] == "zu":
                    aditza = "zakizki"
                if args["Nor"] == "zuek":
                    aditza = "zakizki(zuek)"
                if args["Nor"] == "haiek":
                    aditza = "zaizki"

                
                if args["Nori"] == "niri":
                        aditza = aditza + "da"
                #PREGUNTAR
                """if args["Nori"] == "hiri":
                    aditza = aditza + """
                if args["Nori"] == "hari":
                    aditza = aditza + "o"
                if args["Nori"] == "guri":
                    aditza = aditza + "gu"
                if args["Nori"] == "zuri":
                    aditza = aditza + "zu"
                if args["Nori"] == "zuei":
                    aditza = aditza + "zue"
                if args["Nori"] == "haiei":
                    aditza = aditza + "e"


            if args["Denbora"] == "Iragana":
                print("IRAGANA")
                if args["Nor"] == "ni":
                    aditza = "nenki"
                if args["Nor"] == "hi":
                    aditza = "henki"
                if args["Nor"] == "hura":
                    aditza = "leki"
                if args["Nor"] == "gu":
                    aditza = "genkizki"
                if args["Nor"] == "zu":
                    aditza = "zenkizki"
                if args["Nor"] == "zuek":
                    aditza = "zenkizki(zuek)"
                if args["Nor"] == "haiek":
                    aditza = "lekizki"


                if args["Nori"] == "niri":
                    aditza = aditza + "da"
                #PREGUNTAR
                """if args["Nori"] == "hiri":
                    aditza = aditza + """
                if args["Nori"] == "hari":
                    aditza = aditza + "o"
                if args["Nori"] == "guri":
                    aditza = aditza + "gu"
                if args["Nori"] == "zuri":
                    aditza = aditza + "zu"
                if args["Nori"] == "zuei":
                    aditza = aditza + "zue"
                if args["Nori"] == "haiei":
                    aditza = aditza + "e"

            if aditza.startswith("zakizki(zuek)"):
                aditza = aditza.replace("(zuek)", "")
                aditza = aditza + "te"
            aditza = aditza + "n"

        if args["Modua"] == "Agintera":
            print("AGINTERA")
            if args["Nor"] == "hi":
                aditza = "haki"
            if args["Nor"] == "hura":
                aditza = "beki"
            if args["Nor"] == "zu":
                aditza = "zakizki"
            if args["Nor"] == "zuek":
                aditza = "zakizki(zuek)"
            if args["Nor"] == "haiek":
                aditza = "bekizki"

            if args["Nori"] == "niri":
                    aditza = aditza + "t"
            #PREGUNTAR
            """if args["Nori"] == "hiri":
                aditza = aditza + """
            if args["Nori"] == "hari":
                aditza = aditza + "o"
            if args["Nori"] == "guri":
                aditza = aditza + "gu"
            if args["Nori"] == "zuri":
                aditza = aditza + "zu"
            if args["Nori"] == "zuei":
                aditza = aditza + "zue"
            if args["Nori"] == "haiei":
                aditza = aditza + "e"

            if aditza.startswith("zakizki(zuek)"):
                aditza = aditza.replace("(zuek)", "")
                aditza = aditza + "te"

    if args["Kasua"] == "NOR-NORK":
        print("NOR-NORK")

    if args["Kasua"] == "NOR-NORI-NORK":
        print("NOR-NORI-NORK")
    
    return aditza
print(build({'Aditza': 'None', 'Kasua': 'NOR-NORI', 'Modua': 'Agintera', 'Denbora': 'Oraina', 'Nor': 'zuek', 'Nori': 'guri', 'Nork': None}))
