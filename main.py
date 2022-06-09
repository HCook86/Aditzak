import eel
from app import analyse
from json import dumps

eel.init('views')

def flash(error):
    eel.error(error)

@eel.expose                       
def handleinput(x):
    if x != "" and not " " in x:
        eel.out(dumps(analyse(x)))
    else:
        flash("Aditz laguntzaile batekin sahiatu.")

eel.start('main.html')