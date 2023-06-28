
import random

from Hangman_art import stages
from Hangman_art import logo
from Hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)


lives = 6
print(logo)




display = []
for _ in range(word_length):
    display += "_"


end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()


    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

   
    if guess not in chosen_word:
        lives-=1
        print(f"Incorrect Guess and you have {lives} remaining")
    if lives==0:
        end_of_game=True
        print("You loose! Better Luck Next Time ")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
