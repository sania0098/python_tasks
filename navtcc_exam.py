import random


def guessing_game():
    print("*************Welcome to the Guessing Game!**************")
    print()
    print("****I'm thinking of a number between 1 and 100.****")
    print()

    # Randomly select a number between 1 and 100
    guess_number = random.randint(1, 100)
    attempts = 0

    while True:
        # Ask the user to guess
        try:
            guess = int(input("Enter your guess number: "))
            attempts += 1

            # Provide feedback based on the user's guess
            if guess < guess_number:
                print("The number you enter is  low! Try again.")
            elif guess > guess_number:
                print("The number you enter is high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number {guess_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")


# Start the game
guessing_game()
