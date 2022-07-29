loco=250000
print("Welcome to Banking System.\n")
print("What service you want to use now ?\n")
print("1.New User? Register an account first.")
print("2.Already have an Account?")
choice=int(input("Enter your choice:"))
if (choice==1):
    nam=input("Enter your name :")
    acc=int(input("Please enter your account number :"))
    pho=int(input("Enter your phone number :"))
    pin=int(input("Enter your PIN code :"))
    print(f"Congratulations, {nam}! Account has been created successfully.")
elif(choice==2):
    attempts=0
    while attempts<3:
        acc=int(input("Enter your Account Number :"))
        pin=int(input("Enter your Password :"))
        attempts+=1
        if acc==12345 and pin ==6789:
            while True:
                print("\nLogged in successfully.\n")
                print("Press 1 to deposit money")
                print("Press 2 to withdraw money")
                print("Press 3 to check current balance")
                print("Press 4 to transfer money")
                print("Press 5 to generate MIS on your current balance")
                print("Press 6 to exit \n")
                choi=int(input("Enter your choice :"))
                if (choi==1):
                    amo=int(input("Enter the amount you want to be deposited :₹"))
                    print("Amount deposited successfully.\n")
                    print("Initial amount: ₹250000")
                    print("Current amount : ₹"+str(loco+amo))
                    tran=input("Do you want to continue the transaction ? [y/n] :")
                    if tran=='y':
                        pass
                    elif tran=="n":
                        print("Transaction  Cancelled Successfully.\n")
                        break
                    else:
                        print("Wrong choice! choose between yes and no.")
                elif (choi==2):
                    withd=int(input("Enter the amount you want to be withdrawn :₹"))
                    if withd < loco:
                        print("Please check if ...")
                        def denom_check(amount):
                            denominations=[2000,500,100,50,20,10,5,2,1]
                            for i in range(0,len(denominations)):
                                notes =int(amount/denominations[i])
                                if amount:
                                    amount = amount % denominations[i]
                                    print("There are",notes,": ₹",str(denominations[i])," notes here")
                        denom_check(withd)

                        print("Amount withdrawn successfully.")
                        print("Initial amount: ₹250000")
                        print("Current amount : ₹"+str(loco-withd))   
                        tran=input("Do you want to continue the transaction ? [y/n] :")
                        if tran=='y':
                            pass            
                        elif tran=="n":
                            print("Transaction  Cancelled Successfully.\n")
                            break
                        else:
                            print("Wrong choice! choose between yes and no.")
                    else:
                        print("\n Sorry! You have insufficient balance.")
                elif (choi==3):
                    print("Your current balance is ₹"+str(loco))
                elif (choi==4):
                    acc=int(input("Enter the account number to transfer money :"))
                    ifsc=input("Enter the IFSC :")
                    mon=int(input("Enter the money to be transferred :₹"))
                    print("Initial amount: ₹250000")
                    print("Current amount : ₹"+str(loco-mon))
                    print(f"You have transferred ₹{float(mon)} to account number {acc}")
                    tran=input("Do you want to continue the transaction ? [y/n] :")
                    if tran=='y':
                        pass
                    elif tran=="n":
                        print("Transaction  Cancelled Successfully.\n")
                        break
                    else:
                        print("Wrong choice! choose between yes and no.")
                elif (choi==5):
                    rate=float(input("Enter rate in % :"))
                    tim=int(input("Enter time in years :"))
                    si=loco*rate*tim/100
                    print("Yeary Interest :₹"+str(si))
                    print("Monthly Interest :₹"+str(si/12))
                    tran=input("Do you want to continue the transaction ? [y/n] :")
                    if tran=='y':
                        pass
                    elif tran=="n":
                        print("Transaction  Cancelled Successfully.\n")
                        break
                    else:
                        print("Wrong choice! choose between yes and no.")
                elif (choi<1) or (choi>5):
                    break
            break
        else:
            print(f"Invalid Credentials.You have tried {attempts} times. ")
            while attempts==3:
                print("You can't login now.")
                break 
else:
    print("Wrong Choice! you should choose between 1 and 2")
    

