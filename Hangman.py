
import random
from Words import words




def get_valid_word():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
     word = get_valid_word(words)
     word_letters = set(word)
     alphabet = set(string.ascii_uppercase)
     used_letters = set()

     lives = 6

while len(word_letters) > 0 and lives > 0 :
    print('You have' , lives , 'lives left' , 'You have used these letters: ', ' '.join(used_letters))
    word_list = [letter if letter in user_letter else '-' for letter in word]
    print('Current word: ', ' '.join(word_list))

    user_letter = input("Guess a letter:  ").upper()
    if user_letter in alphabet - user_letters:
        user_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters
        else:
            lives = lives - 1
            print('Letter is not in word')

    elif user_letter in used_letter:
        print('You have already used the letter. Try Again')

    else:
        print("Invalid character. Please Try Again ")

    if lives == 0:
        print("You're out of lives. The word was " , word)
    else:
        print("You guessed the word right", word, '!!')

hangman()