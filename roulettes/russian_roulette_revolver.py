import random
import time


def russian_roulette():
    print("Welcome to Russian Roulette!")
    print("The game begins...")
    print("Spinning the revolver cylinder...")
    time.sleep(2)

    # There are 6 chambers in the cylinder
    chambers = [0, 0, 0, 0, 0, 0]

    # Place a bullet in a random chamber
    bullet_chamber = random.randint(0, 5)
    chambers[bullet_chamber] = 1

    print("The bullet is placed in the revolver.")
    print("Each player will take turns pulling the trigger. Good luck!")

    # Randomly select the starting player
    current_player = random.randint(1, 6)

    while True:
        print(f"Player {current_player}, it's your turn. Press enter to pull the trigger.")
        input()

        if chambers[current_player - 1] == 1:
            print(f"Player {current_player} pulls the trigger... BANG! You're out!")
            break
        else:
            print(f"Player {current_player} pulls the trigger... CLICK! You survived.")

        # Move to the next player
        current_player = (current_player % 6) + 1

    print("Game over!")


# Run the game
russian_roulette()
