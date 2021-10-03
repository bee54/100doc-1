# Auction
#
# Should have used a dictionary type instead of all this stuff with classes


print()
print("(\\") 
print("\\'\\")
print(" \\'\\     __________ ")
print(" / '|   ()_________)")
print(" \\ '/    \\ ~~~~~~~~ \\")
print("   \\       \\ ~~~~~~   \\")
print("   ==).      \\__________\\")
print("  (__)       ()__________))")

print("\nAuction House")
print("=============================================")

class Participant:
  def __init__(self, name, bid):
    self.name = name
    self.bid = bid


def getParticipant():
  
  participantName=input("Enter name: ")

  participantBid=int(input("Bid: $"))

  participant = Participant(participantName, participantBid)

  return participant


# Returns a list of Participant objs, each with a name and a bid 
def gatherParticipantList():

  participantList=[] #Empty list for participants
  

  getNewPariticipant='y' # Gate for getting another participant or moving foward with auction "Gather at least 1 guest"
  
  while(getNewPariticipant=='y'):
    # Get participant info and load 
    participantList.append(getParticipant())
    getNewPariticipant=input("Any other bidders? (y/n) ")

  return participantList


# Get high bid from list of Participant
def getHighestBidFromParticipantList(gatheredParticipantList):
  
  highestBid=0

  winningParticipant=None
  
  for participant in gatheredParticipantList:
    
    if(participant.bid > highestBid):
      
      winningParticipant=participant
  
  return winningParticipant

def printWinner(winningParticipant):
  print(winningParticipant.name, end='')
  print(" won the auction with a bid of $", end='')
  print(winningParticipant.bid, end='')


gatheredParticipantList=gatherParticipantList()


printWinner(getHighestBidFromParticipantList(gatheredParticipantList))

