import random

def play_game():
    # The computer picks a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    win = False

    print("--- Welcome to the Guessing Game! ---")
    print("I'm thinking of a number between 1 and 100.")

    while not win:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Correct! You found it in {attempts} attempts.")
                win = True
        except ValueError:
            print("Please enter a valid whole number.")

if __name__ == "__main__":
    play_game()