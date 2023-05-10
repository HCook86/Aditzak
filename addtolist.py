import os
def rmlastln(filename):
    with open(filename, 'rb+') as filehandle:
        filehandle.seek(-1, os.SEEK_END)
        filehandle.truncate()

def writeln(filename, txt):
    with open(filename, "a") as file:
        file.write(txt + "\n")

def dellastln(file):
    with open(file, "r+") as f:
        current_position = previous_position = f.tell()
        while f.readline():
            previous_position = current_position
            current_position = f.tell()
        f.truncate(previous_position)

verb_caract = ["Aditza", "Kasua", "Modua", "Denbora", "Nor", "Nori", "Nork"]

filename = "verb.ls"
with open(filename, "a") as file:

    writeln(filename, "")
    cmd = ""
    while cmd != "exit":
        cmd = input()

        if cmd == "new":
            print("Aditza tiene que ir entero en minusculas")
            v = []
            for i in verb_caract:
                v.append(input(i + ": "))
            
            writeln(filename, str(dict(zip(verb_caract, v))))
        
        if cmd == "undo":
            dellastln(filename)

    rmlastln(filename)