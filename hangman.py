import random

# Visual stages for the hangman drawing
HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |

     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\  |
    / \  |
        ===""",
]

# Words grouped by category
WORD_BANK = {
    "Animals": ["elephant", "giraffe", "kangaroo", "penguin", "dolphin"],
    "Countries": ["canada", "brazil", "germany", "japan", "australia"],
    "Fruits": ["banana", "strawberry", "pineapple", "mango", "watermelon"],
}


def get_random_word(word_dict):
    # Pick a random category, then a random word from it
    category = random.choice(list(word_dict.keys()))
    word = random.choice(word_dict[category])
    return category, word


def play_round():
    category, word_to_guess = get_random_word(WORD_BANK)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = len(HANGMAN_PICS) - 1

    print(f"\n--- NEW ROUND ---")
    print(f"Category hint: {category}")

    while wrong_guesses < max_wrong:
        # Print the current hangman visual
        print(HANGMAN_PICS[wrong_guesses])

        # Display the word with underscores
        display_word = [
            letter if letter in guessed_letters else "_" for letter in word_to_guess
        ]
        print("Word to guess: " + " ".join(display_word))
        print(f"Incorrect guesses left: {max_wrong - wrong_guesses}")

        # Check if player won
        if "_" not in display_word:
            print(
                f"\n🎉 Victory! You correctly guessed the word: {word_to_guess.upper()}"
            )
            return True

        # Get player guess
        guess = input("Guess a letter: ").lower().strip()

        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input. Please type a single letter.")
            continue
        if guess in guessed_letters:
            print(f"⚠️ You already tried '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        # Check if letter is in the word
        if guess in word_to_guess:
            print(f"✨ Nice! '{guess}' is in the word.")
        else:
            print(f"❌ Oops! '{guess}' is not in the word.")
            wrong_guesses += 1

    # If the loop ends, the player ran out of guesses
    print(HANGMAN_PICS[wrong_guesses])
    print(f"\n💀 Game Over! The word was: {word_to_guess.upper()}")
    return False


def main():
    print("================================")
    print("   WELCOME TO ULTIMATE HANGMAN  ")
    print("================================")

    score = 0
    while True:
        won = play_round()
        if won:
            score += 1

        print(f"Current Score: {score} wins")

        play_again = input("\nWant to play another round? (y/n): ").lower().strip()
        if play_again != "y":
            print(f"\nThanks for playing! Your final score is {score} wins. Goodbye!")
            break


if __name__ == "__main__":
    main()
