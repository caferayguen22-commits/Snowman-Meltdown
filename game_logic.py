import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown", "code", "logic"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    print("\n" * 5)
    print("================================")
    print(STAGES[mistakes]) # Display the snowman stage for the current number of mistakes.

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(f"Word: {display_word}")
    print(f"Guessed so far: {', '.join(guessed_letters)}")
    print("================================")


def play_game():
    while True: # Äußere Schleife zum Wiederholen des Spiels
        secret_word = get_random_word()
        guessed_letters = []
        mistakes = 0
        max_mistakes = len(STAGES) - 1

        print("Welcome to Snowman Meltdown!")

        # Die Spielschleife
        while mistakes < max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters)

            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("❌ Invalid input! Please enter a single letter (a-z).")
                continue

            if guess in guessed_letters:
                print(f"⚠️ You already guessed '{guess}'.")
                continue

            guessed_letters.append(guess)

            if guess in secret_word:
                print(f"Good job! '{guess}' is in the word.")
            else:
                mistakes += 1
                print(f"❌ Oh no! '{guess}' is not there.")

            # Prüfen, ob alle Buchstaben erraten wurden
            if all(letter in guessed_letters for letter in secret_word):
                display_game_state(mistakes, secret_word, guessed_letters)
                print("🎉Congratulations! You saved the snowman!")
                break

        else:
            display_game_state(mistakes, secret_word, guessed_letters)
            print("💀 GAME OVER! The snowman has melted.")
            print(f"The word was: {secret_word}")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    play_game()