#I had to use a lot of float casts for this...
# Designed to run once for one set of data





billTotalFloat=float(input("Enter Bill total: "))

splitYN=input("Split Bill? y/n")


#Will be replaced with any new per-payer bill total
billTotalPerPayer=float(billTotalFloat)


if splitYN.lower() in ['y','ye','yes']:
  sad=True
  splitBy=input("Enter divisor for bill split: ")
  billTotalPerPayer=billTotalPerPayer / float(splitBy)

taxAsInt=float(input("Enter tax as percent int: "))


finalValue=round((billTotalPerPayer + billTotalPerPayer*taxAsInt*0.01),2)


print(finalValue)


