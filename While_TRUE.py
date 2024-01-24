import random
lives = 3

while True:
    print(f"You have {lives} lives left")
    dice_roll = random.randint(1,6)
    if dice_roll == 0:
        print("You lost all your lives, game over.")
        break
    if dice_roll == 6:
        print("You rolled a 6, you win!")
        break

    print(f"You rolled a {dice_roll}, try again.")
    lives -= 1