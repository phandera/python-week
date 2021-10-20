print("GUESSING GAME")
guess=int(input("Guess a any number : "))

newSet = set()
i=1;
max=9

while i<=max :
    newSet.add(str(i))
    i+=1

computerGuess=int(list(newSet)[0])

while guess!=computerGuess :
  guess=int(input("You have entered wrong guess, please enter again : "))
else:print("Well guessed!")



