# -*- coding: utf-8 -*-
import random
"""
Similar to hangman this game is called guess the pizza type
Created on Fri Oct 18 13:52:50 2024
@author: JHarris
"""
stages= [":",":-",":-)",":-D","X-D"]

word_list = ["dishes","vacuum", "mop", "dust","steam","organize"]
# Randomly choose a word from the word_list and assign it to a variable called chosen_word
#variuable that represents the lives
lives = 5
chosen_word= random.choice(word_list)

print(chosen_word)
# Create a placeholder with the same number of blanks as the chosen_word
placeholder=""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_ "
print(placeholder)
#use a while loop to let the user guess again
game_over = False

correct_letters = []


while not game_over:
    #Ask the user to guess a lettter and assign their
    guess = input("Guess the chores pick a letter:").lower()
    #create a display that puts the guessed letter in the right positions and "_" in the right position
    if guess in correct_letters:
        print(f"Youve already guessed {guess}")
    display = ""
    #change the for loop so you can keep the previously guesssed words
    #check if the letter the user guessed is Right/ WRONG then print "RIGHT" orPrint "WRONG" if its not
    for letter in chosen_word :
        if letter == guess: 
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
            
            
    print (display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose************")
    if "_" not in display:
        game_over = True
        print("WINNER**************")
        
        
    print(stages[lives])