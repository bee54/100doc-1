# Password Gen
# I know people don't like camel case in python but because PyCharm decided to voice an opinion about it, I am making sure to continue to use camelCase for python forever. I can't believe an IDE is programmed to give me it's opnion on my variable names.

import random
import os



# Instance vars
passLength=32




def generatePassword(passLength):

    password = ""

    random.seed(os.urandom(999))

    for x in range(0, int(passLength)):    # Python didnt know that passLength was an int
        nextChar = random.randint(32, 127)
        password = password + chr(nextChar)

    return password



# Get pass size from user, Enter specifies default
userInputPassLength=input("Password length? (Enter for default)")
if len(userInputPassLength) != 0:
  passLength=userInputPassLength

# Generate Password
print("=New password below=")

print(generatePassword(passLength))

