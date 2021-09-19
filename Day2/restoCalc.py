#I had to use a lot of float casts for this...
# Designed to run once for one set of data


def getBilTotalStdin(billTotalFloat=-1):
  while billTotalFloat < 0:
    billTotalFloat = float(input("Bill total: "))
  
  return billTotalFloat


billTotalFloat=getBilTotalStdin()

splitYN=input("Split Bill? y/n")


#Will be replaced with any new per-payer bill total
billTotalPerPayer=float(billTotalFloat)


if splitYN.lower() in ['y','ye','yes']:
  splitBy=input("Enter divisor for bill split: ")
  billTotalPerPayer=billTotalPerPayer / float(splitBy)

taxAsInt=float(input("Enter tax as percent int: "))


finalValue=round((billTotalPerPayer + billTotalPerPayer*taxAsInt*0.01),2)


print(finalValue)


