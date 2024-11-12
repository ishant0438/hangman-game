import random

# List of possible words
words = ["python", "hangman", "computer", "science", "programming", "developer", "algorithm"]

# Function to choose a random word
def get_random_word(words):
    return random.choice(words)

# Hangman game function
def hangman():
    word = get_random_word(words).upper()
    word_letters = set(word)  # Letters in the word
    alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    used_letters = set()  # Letters guessed by the user
    
    lives = 6  # Number of lives
    
    # Main game loop
    while len(word_letters) > 0 and lives > 0:
        # Display current guessed letters and lives
        print("You have", lives, "lives left and you have used these letters:", " ".join(used_letters))
        
        # Display current word with guessed letters revealed
        word_display = [letter if letter in used_letters else '-' for letter in word]
        print("Current word:", " ".join(word_display))
        
        # Get user input
        user_letter = input("Guess a letter: ").upper()
        
        # Check if user letter is valid
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"Good guess! '{user_letter}' is in the word.")
            else:
                lives -= 1
                print(f"Oops! '{user_letter}' is not in the word.")
        elif user_letter in used_letters:
            print("You have already used that letter. Try again.")
        else:
            print("Invalid character. Please enter a letter.")
    
    # Outcome of the game
    if lives == 0:
        print("You lost! The word was:", word)
    else:
        print("Congratulations! You guessed the word:", word)

# Run the game
hangman()
