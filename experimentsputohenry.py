filename = "verb.ls"

verbs = []

with open(filename, "r") as file:
    verbs = file.read().split("\n")

verbs = list(map(eval, verbs))

currentVerbs = []
for i in verbs:
    currentVerbs.append(i["Aditza"])

#NOMBRE HORRIBLE, CAMBIAR EN VERSION CUANDO HENRY HAGA COMMIT
verbtocheck = "kdjasdba"
if verbtocheck in currentVerbs:
    for i in verbs:
        if (verbtocheck == i["Aditza"]):
            print(i)
            break