def denom_check(amount):
    denominations=[2000,500,100,50,20,10,5,2,1]
    for i in range(0,len(denominations)):
        notes =int(amount/denominations[i])
        if amount:
            amount = amount % denominations[i]
            print("There are",notes,":",denominations[i],"rupees notes here")
amt=int(input("Enter the Amount :"))
denom_check(amt)
