import eel
from app import analyse

eel.init('views')

def flash(error):
    eel.error(error)

@eel.expose                       
def handleinput(x):
    if x != "" and not " " in x:
        eel.out(str(analyse(x)))
    else:
        flash("Aditz laguntzaile batekin sahiatu.")

eel.start('main.html')