from random import randint
print("GUESSSING GAME")
guess=int(input("Guess a any number : "))

computerGuess=randint(1, 9)

while guess!=computerGuess :
  guess=int(input("You have entered wrong guess, please enter again : "))  
else:print("Well guessed!")



