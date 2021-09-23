import random



#Rock Paper Scissors. One round
rounds=int(input("How many Rock Paper and Scissors can you take?"))
#^^ It turns out int can't take a decimal so its just typing without any boxing


def getUserInputs():
  return input("Type 0 for rock, 1 for paper, 2 for scissors:\nUser choice: ") # game string 1


def runGame():

  userChoice=int(getUserInputs())

  computerChoice=random.randint(0, 2)

  print(f"Computer choice: {computerChoice}") # Is this better or worse than "" + var. It's worse right? It looks a lot worse and its harder to the {} chars on a keyboard. It works when print says it cant concat a string and an int.

  if computerChoice == userChoice:
    print("Two losers don't make a winner.")
  elif computerChoice < userChoice:
    print("computerChoice  < userChoice")
  else:
    print("computerChoice  > userChoice, hopefully")



#Run 
for x in range(0, rounds):
  runGame()
