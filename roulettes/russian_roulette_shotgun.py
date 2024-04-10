import random
import time

def russian_roulette_shotgun():
    print("Welcome to Shotgun Russian Roulette!")
    print("The game begins...")
    time.sleep(2)

    # There are 2 chambers in the shotgun
    chambers = [0, 0]

    # Place a shell in a random chamber
    bullet_chamber = random.randint(0, 1)
    chambers[bullet_chamber] = 1

    print("The shell is placed in the shotgun.")
    print("Each player will take turns pulling the trigger. Good luck!")

    # Randomly select the starting player
    current_player = random.randint(1, 2)

    while True:
        print(f"Player {current_player}, it's your turn. Press enter to pull the trigger.")
        input()

        if chambers[current_player - 1] == 1:
            print(f"Player {current_player} pulls the trigger... BOOM! You're out!")
            break
        else:
            print(f"Player {current_player} pulls the trigger... CLICK! You survived.")

        # Move to the next player
        current_player = (current_player % 2) + 1

    print("Game over!")

# Run the game
russian_roulette_shotgun()
