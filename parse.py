import sys
import re

filename = sys.argv[1]

with open(filename) as file:
    for line in file:
        if not line[0]=="#" and line.strip():
            args = re.split(r"\s[-]\s", line.strip())
            if len(args) == 2:
                command = args[0].strip(' `')
                action = args[1].strip()
                print("command: {} action: {}".format(command, action))
