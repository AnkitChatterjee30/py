print("Create Account now ")
username=input("Enter user name : ")
password=input("Enter the password : ")

print("Your account has been created successfully. ")
print("Login now ")
attempts=0
while attempts <3:
    username2=input("Enter username : ")
    password2=input("Enter the password : ")
    attempts+=1
    if username==username2 and password==password2:
        print("Logged in successfully")
        break
    else:
        print(f"Invalid Credentials.You have tried {attempts} times. ")
while attempts==3 and password!=password2:
    print("You can't login now. ")
    break
