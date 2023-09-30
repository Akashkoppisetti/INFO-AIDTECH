import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    name = input("What's your name? ")
    print(f"Hello, {name}! Let's play a game.")
    print("I'm thinking of a number between 1 and 100. You have 10 attempts to guess it.")

    play_again = True

    while play_again:
        secret_number = random.randint(1, 100)
        attempts = 0

        while attempts < 10:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess (between 1 and 100): "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations, {name}! You guessed the number {secret_number} in {attempts} attempts.")
                break

        if attempts >= 10:
            print(f"Game over, {name}! The number was {secret_number}.")

        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        play_again = play_again_input == 'yes'

if __name__ == "__main__":
    number_guessing_game()