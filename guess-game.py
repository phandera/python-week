#This game is fine however I was expecting that you use the knowledge that I taught you. Please create another version of this game that does not use the random module.

from random import randint
print("GUESSING GAME")
guess=int(input("Guess a any number : "))

computerGuess=randint(1, 9)

while guess!=computerGuess :
  guess=int(input("You have entered wrong guess, please enter again : "))
else:print("Well guessed!")



