
# Does finalValue for single payer equal sum of all finalValues for multiple payers? Yes

#



###
### New Findings
###
# Does not filter for negative input


def getTaxStdin():
  return float(input("Enter tax as percent int: "))# tax req text

def getBillTotalStdin():
  return float(input("Enter Bill total: ")) 

def getSplitByStdin():
  return input("Split bill by: ") #splitBy req text



def billCalcDriver(billTotalFloat,splitBy,taxAsInt):

  #billTotal req text

  #Maybe drop this
  #splitYN=input("Split Bill? y/n")
  splitYN='y'

  #Will be replaced with any new per-payer bill total
  billTotalPerPayer=float(billTotalFloat)


  if splitYN.lower() in ['y','ye','yes']:
    billTotalPerPayer=billTotalPerPayer / float(splitBy)

  


  return round((billTotalPerPayer + billTotalPerPayer*taxAsInt*0.01),2)



#Print assert true
print(billCalcDriver(100,5,15)*5==billCalcDriver(100,1,15))


