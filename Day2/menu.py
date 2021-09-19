
#So far failing to build a menu
print("Which file: ")
print("1 restoCalc_Test.py")
print("2 restoCalc.py")
inpu=input(": ")
if inpu in (1,1) :
  import restoCalc_Test
  print(restoCalc_Test.finalValue)
elif inpu in (2,2):
  import restoCalc
  print(restoCalc.finalValue)