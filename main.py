import eel
from app import analyse
from json import dumps

eel.init('views')

def flash(error):
    eel.error(error)

@eel.expose                       
def handleinput(x):
    if x != "" and not " " in x:
        x = analyse(x)

        if x["Kasua"] == "NOR":
            if x ["Nor"] != None and x ["Nori"] == None and x ["Nork"] == None:
                eel.out(dumps(x))
            else:
                flash("Aditz hau ez da existitzen.")

        if x["Kasua"] == "NOR-NORI":
            if x ["Nor"] != None and x ["Nori"] != None and x ["Nork"] == None:
                eel.out(dumps(x))
            else:
                flash("Aditz hau ez da existitzen.")

        if x["Kasua"] == "NOR-NORK":
            if x ["Nor"] != None and x ["Nori"] == None and x ["Nork"] != None:
                eel.out(dumps(x))
            else:
                flash("Aditz hau ez da existitzen.")

        if x["Kasua"] == "NOR-NORI-NORK":
            if x ["Nor"] != None and x ["Nori"] != None and x ["Nork"] != None:
                eel.out(dumps(x))
            else:
                flash("Aditz hau ez da existitzen.")

    else:
        flash("Aditz laguntzaile batekin sahiatu.")

eel.start('main.html')
