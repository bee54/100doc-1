import random



#Rock Paper Scissors. One round
rounds=int(input("How many games of Rock Paper and Scissors can you take?"))
#^^ It turns out int can't take a decimal so its just typing without any boxing



def getUserInputs():
  return input("Type 0 for rock, 1 for paper, 2 for scissors:")



def runGame():

  playerChoice=int(getUserInputs())
  computerChoice=random.randint(0, 2)

  # Print inputs
  print(f"Computer: {computerChoice}                 {playerChoice}: User")


  #Winner decider

  if computerChoice == playerChoice: # If its a tie
    print("Tie")
  elif computerChoice > playerChoice or (computerChoice % 2 == playerChoice): # IF computerChoice==2
    print("Computer WINS")
  elif computerChoice > playerChoice or computerChoice  == playerChoice % 2:  # IF playerChoice==2
    print("Player WINS")








#Run 
for x in range(0, rounds):
  runGame()
