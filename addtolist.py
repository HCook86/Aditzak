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

    cmd = ""
    while cmd != "exit":
        cmd = input()

        if cmd == "new":
            v = []
            for i in verb_caract:
                v.append(input(i + ": "))
            
            writeln(filename, str(dict(zip(verb_caract, v))))
        
        if cmd == "undo":
            dellastln(filename)