#
# Generate a creative business name
#
#

def scramble(petNameFromMain, randomizerSeedFromMain):
  for x in range(0, length(petName)):
    petName[x]++
  return petName


print("Alternative business name generator: ")

# Get inputs for business name
cityName = input("Input a name for a city: ")
petName = input("Input a name for a pet: ")
randomizerSeed=int(input("Enter an int: "))

print(cityName + scramble(petName, randomizerSeed))
