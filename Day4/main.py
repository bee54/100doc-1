import random



#Rock Paper Scissors. One round
rounds=int(input("How many Rock Paper and Scissors can you take?"))
#^^ It turns out int can't take a decimal so its just typing without any boxing



def getUserInputs():
  return input("Type 0 for rock, 1 for paper, 2 for scissors:\nUser choice: ") # game string 1



def runGame():

  userChoice=int(getUserInputs())
  computerChoice=random.randint(0, 2)


  print(f"Computer choice: {computerChoice}")


  if computerChoice == userChoice:
    print("Two losers don't make a winner.")
  elif computerChoice < userChoice:
    print("#################")
    print("#               #")
    print("# Computer wins #")
    print("#               #")
    print("#################")
    #print("computerChoice  < userChoice")
  elif computerChoice < userChoice-1:
    print("#################")
    print("#               #")
    print("# Computer wins #")
    print("#               #")
    print("#################")
    #print("computerChoice  < userChoice")
  elif computerChoice > userChoice:
    print("#################")
    print("#               #")
    print("# User     wins #")
    print("#               #")
    print("#################")
    #print("computerChoice  > userChoice, hopefully")



#Run 
for x in range(0, rounds):
  runGame()
