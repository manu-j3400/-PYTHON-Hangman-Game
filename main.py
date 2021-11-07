import os
import time

player1 = input("What your name: ")
print("ok " + player1 + " the game will start momentarily....")

# Puts a delay

time.sleep(1)


# Clears the screen to make it look good

clear = lambda: os.system('clear')

clear()

temp = "_"
# trueword is word that's supposed to be guessed
trueWord = input(player1 + ", enter a word: ")

#guessCollection to keep track of words guessed

lives = 5
guessCollection = []

#guessword is to keep track of the length of the word and the number of underscores
guessWord = ["_"] * len(trueWord)

isGameComplete = False


while not isGameComplete:

  print("".join(guessWord))


  # Letter that player is going to guess

 
  letterGuess = input(player1 + ", please put your guess: ")
      
  
  if letterGuess in trueWord:

    guessCollection.append(letterGuess)
  
    for idx, char in enumerate(trueWord):  # go through the word (remembering the index)
  
        if char == letterGuess:             # check if it is a match
  
            guessWord[idx] = letterGuess    # print the result

  elif letterGuess not in trueWord:
    lives -= 1

    guessCollection.append(letterGuess)
  
    print(f"\nWhoops now you only have {lives} lives left!\n")
  
  if guessWord == trueWord:
  
    print("YOU HAVE WON THE GAME!")
  
    isGameComplete = True
  
    break

  if lives == 1:
    print("Sorry you died!")
    
    break
    
    
    