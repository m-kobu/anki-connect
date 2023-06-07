import sys
import re
import json

filename = sys.argv[1]

# toDo: to read lines of variable number of elements in a line
with open(filename) as file:
    meta = file.readline()
    if meta[0] == "#":
        name = meta.strip(" #\n")
        print(name)
        with open(name+".json") as jsonfile:
            data = json.load(jsonfile)
            for i in data["fields"]:
                print(i)
    for line in file:
        if line.strip():
            args = re.split(r"\s[-]\s", line.strip())
            x = dict(zip(data["fields"], args))
            print(x)

#            if len(args) == 2:
#                command = args[0].strip(' `')
#                action = args[1].strip()
#                print("command: {} action: {}".format(command, action))

# the output of that file needs to be in the form [{elements in the line}]
                
