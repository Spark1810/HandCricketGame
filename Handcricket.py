# Hand Cricket Game By Sudharshan Vijay SK
# Njoy the game...

import random
 
def play_hand_cricket():
    print("Welcome to Hand Cricket!")
    print("Rules: You and the computer will take turns batting and bowling.")
    print("When batting, enter a number from 1 to 6 to score runs.")
    print("If your number matches the computer's number while batting, you're out!")
    print("Try to score as many runs as possible!")
    print("Let's begin!") 

    total_runs = 0              # Your Score
    computer_total_runs = 0     # Computers Score

    while True:
        # Player's turn
        player_num = int(input("Enter your batting number (1-6): "))
        computer_num = random.randint(1, 6)

        if player_num < 1 or player_num > 6:
            print("Invalid input. Try again.")
            continue

        print("Your number:", player_num)
        print("Computer's number:", computer_num)

        if player_num == computer_num:
            print("Out!")
            break
        else:
            total_runs += player_num
            print("Your runs:", total_runs)

        # Computer's turn
        computer_num = random.randint(1, 6)
        player_num = int(input("Enter your bowling number (1-6): "))

        if player_num < 1 or player_num > 6:
            print("Invalid input. Try again.")
            continue

        print("Your number:", player_num)
        print("Computer's number:", computer_num)

        if player_num == computer_num:
            print("Computer is out!")
            break
        else:
            computer_total_runs += computer_num
            print("Computer's runs:", computer_total_runs)

    print("Game over!")
    print("Your total runs:", total_runs)
    print("Computer's total runs:", computer_total_runs)

    if total_runs > computer_total_runs:
        print("Congratulations! You win!")
    elif total_runs < computer_total_runs:
        print("You lose! Better luck next time!")
    else:
        print("It's a tie!")

play_hand_cricket()
