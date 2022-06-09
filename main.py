import eel
from app import analyse

eel.init('views')

@eel.expose                         # Expose this function to Javascript
def handleinput(x):
    eel.out(str(analyse(x)))
    #eel.display()

eel.start('main.html')
