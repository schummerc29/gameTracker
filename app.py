# Declare all imports
import sqlite3
import time 


con = sqlite3.connect("games.db")
cur = con.cursor()
print("Checking database for table...")
time.sleep(2)
try:
    cur.execute("CREATE TABLE library(Game, System, Start, End, Rate)")
except sqlite3.OperationalError:

    print("Library table already exists")


delete = input("Do you want to reset your library? (Y/N): ")
if delete == 'Y':
    confirm = input("Are you absolutely sure (will delete ALL games in library)? (Y/N): ")
    if confirm == 'Y':
        cur.execute('''DELETE FROM library''')

# Declare list and dictionary
library = []
game = {}
ask = ''


# Prompts for game info, adds to library then clears dictionary
while True:    
    name = input("What game do you want to add?: ")
    system = input(f"What system did you play {name} on?: ")
    start = input("When did you start playing?: ")
    end = input("When did you finish playing?: ")
        
    while True:
        try:
            rate = int(input(f"What do you rate {name} 1-10?: "))
        except ValueError:
            print("Please enter a number between 1 and 10")
            continue
        else:
            break

    game["Game"] = name
    game["System"] = system
    game["Start Date"] = start
    game["Completed / Abandoned Date"] = end
    game["Rating"] = rate

    cur.execute('''
          INSERT INTO library (Game, System, Start, End, Rate)
            VALUES (?, ?, ?, ?, ?)''', (name, system, start, end, rate))


    print("   ")
    print("Adding game to library...")
    time.sleep(3)
    print(f"{name} has been added to your libaray!")
    print("  ")
    time.sleep(1)
    ask = str(input("Do you want to enter another game?: "))
    if ask == "yes":
        continue
    else:
        game = {}
        break


# Fetch All distinct Rows in Library table
statement = '''SELECT DISTINCT * FROM library'''
cur.execute(statement)

print("  ")
print("Reading table data:")
output = cur.fetchall()
for row in output:
    print(row)
con.commit()


# Close connection to DB
print("   ")
print("Closing connection...")
try:
    con.close()
    time.sleep(2)
except sqlite3.OperationalError as e:
    print(e)
else:
    print("Connection closed")