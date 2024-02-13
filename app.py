# Declare all imports
import sqlite3
import time 
from datetime import date, datetime


con = sqlite3.connect("games.db")
cur = con.cursor()
print("Checking database for table...")
time.sleep(2)
try:
    cur.execute("CREATE TABLE library(Game, System, Start, End, Rate)")
except sqlite3.OperationalError:

    print("Library table already exists")


delete = input("Do you want to reset your library? (Y/N): ")
if delete.upper() == "Y":
    confirm = input("Are you absolutely sure (will delete ALL games in library)? (Y/N): ")
    if confirm.upper() == 'Y':
        cur.execute('''DELETE FROM library''')

# Declare list and dictionary
library = []
game = {}
ask = ''
current_date = datetime.today()


# Prompts for game info, adds to library then clears dictionary
while True:    
    name = input("What game do you want to add?: ")

    while True:
        system = input(f"What system did you play {name} on?: ")
        if (system == 'PlayStation') or (system == 'Xbox') or (system == 'PC') or (system == 'Nintendo'):
            break
        else:
            print("Please enter PlayStation, Xbox, PC, or Nintendo")
            continue


    #while True:
    start = input("When did you start playing?: ")
        #start = datetime.strptime(start, '%m/%d/%y')
        #if (start >= current_date):
        #   print("Please enter date earlier than or equal to today")
        #    continue
        #else:
        #    break


    #while True:
    end = input("When did you finish playing?: ")
        #end = datetime.strftime(end, '%m/%d/%y')
        #if (end <= start):
        #    print("Please enter a date later than the start date")
        #    continue
        #else:
        #    break

    while True:
        try:
            rate = int(input(f"What do you rate {name} 1-10?: "))
            if 0 <= rate <= 10:
                break
            raise ValueError()
        except ValueError:
            print("Please enter a valid number")
            continue


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