import sys
import re
import json
from invoke import invoke

filename = sys.argv[1]

# toDo: to read lines of variable number of elements in a line
with open(filename) as file:
    meta = file.readline()
    if meta[0] == "#":
        name = meta.strip(" #\n")
        print(name)
        with open(name+".json") as jsonfile:
            data = json.load(jsonfile)
            result_add_deck = invoke("createDeck", deck=data["deckName"])
    for line in file:
        if not line[0] == "$" and line.strip():
            args = re.split(r"\s[-]\s|[;]", line.strip())
            x = dict(zip(data["fields"], args))
            print(x)
            result_add_note = invoke("addNotes", notes=[{"deckName":data["deckName"], "modelName":data["modelName"], "fields": x, "tags":[]}])
            print(result_add_note)


# the output of that file needs to be in the form [{elements in the line}]
                
