import random

def hangman():
    words = ['python', 'hangman', 'game', 'programming', 'random', 'computer']

    # Select a random word from the list
    word = random.choice(words)

    # Set up the game
    guesses = []
    tries = 6

    # Game loop
    while tries > 0:
        # Display the current state of the word
        display_word = ''
        for letter in word:
            if letter in guesses:
                display_word += letter
            else:
                display_word += '_ '
        print(display_word)

        # Check if the player has guessed all the letters
        if '_' not in display_word:
            print('Congratulations! You guessed the word correctly.')
            break

        # Prompt the player for a guess
        guess = input('Enter a letter: ').lower()

        # Check if the letter has already been guessed
        if guess in guesses:
            print('You have already guessed that letter.')
            continue

        # Add the letter to the list of guesses
        guesses.append(guess)

        # Check if the letter is in the word
        if guess in word:
            print('Correct guess!')
        else:
            print('Wrong guess!')
            tries -= 1
            print('Tries left:', tries)

    # Check if the player lost
    if tries == 0:
        print('You lost. The word was', word)

# Start the game
hangman()
