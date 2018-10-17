import json
from difflib import *

data = json.load(open("data.json"))


def definition(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        prompt = input("Did you mean {0} ? Enter[Y/N]".format(get_close_matches(w, data.keys())[0]))
        if prompt == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif prompt == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "Your word doesn't match."
    else:
        return "The word doesn't exist please enter another word."


word = input("Enter word:")

output = definition(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)


