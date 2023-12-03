import random
import string

difficulty = 0
remaining_lives = 0
 
while difficulty not in ["e", "m", "h"]:
    difficulty = input("Do you want to play on easy(e), medium(m), or hard(h) mode? ")
with open("D:/Phyton/vicceskedés/12 begginer projects/hangman/koviubi.txt", "r") as file:
    file_content = file.read()
words = file_content.split()
words = words

if difficulty == "e":
    remaining_lives = 12; filtered_words = [word for word in words if 3 < len(word) <= 5]
elif difficulty == "m":
    remaining_lives = 8; filtered_words = [word for word in words if 5 < len(word) <= 8]
else:
    remaining_lives = 6; filtered_words = [word for word in words if len(word) >= 10]
choosen_word= random.choice(filtered_words)
        
translator = str.maketrans("", "", string.punctuation)
cleansed_word = choosen_word.translate(translator)

#print(f"The chosen word is: {choosen_word}")
#print(f"The cleaned word is: {cleansed_word}")

game_word = cleansed_word
guessed = []

guessed_status = {char: False for char in game_word}



while not all(guessed_status.values()) and remaining_lives > 0:

    display_word = ''.join([char if guessed_status[char] else '_' for char in game_word])
    print(f"Current state: {display_word}")
    print(f"Guessed letters:  {', '.join(guessed)}")
    print(f"Lives:", remaining_lives * "♥")

    
    guess = input("Enter a letter: ")

    
    if len(guess) == 1:
        
        if guess in game_word:
            if not guessed_status[guess] and guess.isalpha():
                print(f"Good guess! '{guess}' is in the word.")
                guessed_status = {char: True if char == guess else status for char, status in guessed_status.items()}
                guessed.append(guess)
            else:
                print(f"Sorry, '{guess}' has already been guessed.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            remaining_lives -= 1  # Reduce the number of lives for incorrect guesses
            print(f"Remaining lives: {remaining_lives}")
            guessed.append(guess)
    else:
        print("Guess a letter: ")
# Check the end condition
if all(guessed_status.values()):
    print(f"Congratulations! You guessed the word: {cleansed_word}")
else:
    print(f"Sorry, you ran out of lives. The correct word was: {cleansed_word}")