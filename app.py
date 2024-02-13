# Declare all imports
import json
import sqlite3
import time
from os import path
from functions import game_input
#import pandas as pd 


con = sqlite3.connect("games.db")
cur = con.cursor()
print("Checking database for table...")
time.sleep(2)
try:
    cur.execute("CREATE TABLE library(Game, System, Start, End, Rate)")
except sqlite3.OperationalError:

    print("Library table already exists")


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
print("Adding data to library: ")
for x in library:
    print(x)

# Parameterize and insert correct values in library table
for x in library:
    for key, value in x.items():
        game = x["Game"]
        system = x["System"]
        start = x["Start Date"]
        end = x["Completed / Abandoned Date"]
        rate = x["Rating"]
        cur.execute('''
          INSERT INTO library (Game, System, Start, End, Rate)
            VALUES (?, ?, ?, ?, ?)''', (game, system, start, end, rate))
# Adding each game five times....need to resolve
        


# Fetch All distinct Rows in Library table
statement = '''SELECT DISTINCT * FROM library'''
cur.execute(statement)

print("Reading table data:")
output = cur.fetchall()
for row in output:
    print(row)
con.commit()


# Close connection to DB
print("Closing connection...")
try:
    con.close()
    time.sleep(2)
except sqlite3.OperationalError as e:
    print(e)
else:
    print("Connection closed")