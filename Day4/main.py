import random
import time

#Rock Paper Scissors. One round


def getUserInputs():
  return input("Type 0 for rock, 1 for paper, 2 for scissors:\nUser choice: ") # game string 1


def runGame():

  userChoice=getUserInputs()

  computerChoice=random.randint(0, 2)

  print(f"Computer choice: {computerChoice}") # Is this better or worse than "" + var. It's worse right? It looks a lot worse and its harder to the {} chars on a keyboard. It works when print says it cant concat a string and an int.

  if computerChoice == userChoice:
    print("Two losers don't make a winner.")
  elif computerChoice  < userChoice:
    



for x in range(0,10):
  runGame()




# elif computerChoice < userChoice and :
#     print("Computer wins")
#     print("Computer has {computerChoice} and user has {userChoice}")
#   else:
#     print("User wins")