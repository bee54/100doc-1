#
# Generate a creative business name
#
#

def scramble(petNameFromMain, randomizerSeedFromMain):
  
  petNameRandomizerString=""


  for x in range(0, len(petNameFromMain)):
    petNameRandomizerString += chr(ord(petNameFromMain[x]) + randomizerSeedFromMain)
  return petNameRandomizerString


print("Alternative business name generator: ")

# Get inputs for business name
cityName = input("Input a name for a city: ")
petName = input("Input a name for a pet: ")
randomizerSeed=int(input("Enter an int: "))

print(cityName[1:len(cityName):] + cityName[0] + " " + scramble(petName, randomizerSeed))
