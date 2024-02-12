# Declare all imports
from functions import game_input
import json
from os import path
import pandas as pd 
import sqlite3


# Declare list and dictionary
filename = 'library.json'
library = []
game = {}
ask = ''


# Prompts for game info, adds to library then clears dictionary
while True:
    game_input(game)
    library.append(game)
    with open(filename, 'w') as json_file:
        json.dump(library, json_file, indent=2, separators=(',', ': '))

    game = {}
    print(" ")
    ask = str(input("Do you want to enter another game?: "))
    if ask == "yes":
        continue
    else:
        game = {}
        break


# Open json file and review entries
with open (filename) as f:
    data = json.load(f)
    print("JSON Data unloaded: ")
    print(data)


# Iterates through list of dictionaries and prints them out
print("   ")
print("   ")
print("Game Data Added: ")
for x in library:
    print(x)