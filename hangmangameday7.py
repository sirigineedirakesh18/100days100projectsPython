import random

# Word list and random word selection
word_list = ['aardvark', 'baboon', 'camel']
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Game setup
display = "_" * word_length
lives = 6
game_over = False

print("🎉 Welcome to Hangman! You have 6 lives.")
print("Word:", ' '.join(display))

# Game loop
while not game_over:
    guess = input("Guess a letter: ").lower()
    new_display = ""
    guess_correct = False

    # Update the display with guessed letters
    for i in range(word_length):
        if chosen_word[i] == guess:
            new_display += guess
            guess_correct = True
        else:
            new_display += display[i]

    if not guess_correct:
        lives -= 1
        print(f"❌ Wrong guess. Lives left: {lives}")
    else:
        print("✅ Correct guess!")

    display = new_display
    print("Word:", ' '.join(display))

    # Check win/loss condition
    if "_" not in display:
        print(f"🎉 You win! The word was: {chosen_word}")
        game_over = True
    elif lives == 0:
        print(f"💀 You lost! The word was: {chosen_word}")
        game_over = True
