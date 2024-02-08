from functions import input_for_game

# Define Dictionary
game = {
    "Game": "",
    "System" : "",
    "Start Date" : "",
    "Completed / Abandoned Date" : "",
    "Rating (1-5)" : ""
}

# Takes user input, assigns values
input_for_game(game)

for x in game.values():
    print(x)
