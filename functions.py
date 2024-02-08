def input_for_game(game):
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
    game["Rating (1-5)"] = rate