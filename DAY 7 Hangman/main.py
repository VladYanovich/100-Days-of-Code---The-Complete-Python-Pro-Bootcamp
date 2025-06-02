import random
import hangman_words
import hangman_art
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = hangman_art.logo
word_list = hangman_words.word_list

print(logo)
chosen_word = random.choice(word_list)
#print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

display = placeholder
display = list(display)

guessed_letters = []

lives = 6

while "".join(display) != chosen_word or lives == 0:
    print(f"guessed letters are: {" ".join(guessed_letters)}")
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print(f"You have already chosen a letter {guess}")
    else:
        p = 0
        guessed_letters.append(guess)
        for letter in chosen_word:
            if letter == guess:
                display[p] = letter
            p += 1
        if guess not in chosen_word:
            lives -= 1
        print("".join(display))
        print(f"Left {lives} lives")
        print(stages[lives])
        if lives == 0:
            print("You Lose")
            print(f"The hidden word is {chosen_word}")
            break
        elif "".join(display) == chosen_word and lives != 0:
            print("You Win")
            break



