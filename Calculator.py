import math
def add(w,v):
    return w+v
def mul(a,b):
    return a*b
def sub(p,q):
    return p-q   
def div(m,n):   
    return m/n   
def exp(d,e):    
    return pow(d,e)
def log(q):
    return math.log(q)   
print("WELCOME TO A SIMPLE MENSURATION PROGRAM")  
while True:  
    print("\nMAIN MENU")  
    print("1. Calculate Addition")  
    print("2. Calculate Multiplication")  
    print("3. Calculate Division")  
    print("4. Calculate Subtraction ")
    print("5. Calculate Exponentiation ")
    print("6. Calculate Logarithmic ")
    print("7. Calculate Cosine")
    print("8. Calculate Sine")
    print("9. Calculate Tangent")
    print("10. Exit")
    choice = int(input("Enter the Choice:"))  
    if(choice==1):
        x=float(input("Enter the first number :"))
        y=float(input("Enter the second number :"))
        print("Result is",add(x,y))    
    elif(choice==2):
        x=float(input("Enter the first number :"))
        y=float(input("Enter the second number :"))
        print("Result is",mul(x,y))
    elif(choice==3):
        x=float(input("Enter the first number :"))
        y=float(input("Enter the second number :"))
        print("Result is",div(x,y))
    elif(choice==4):
        x=float(input("Enter the first number :"))
        y=float(input("Enter the second number :"))
        print("Result is",sub(x,y))
    elif(choice==5):
        x=float(input("Enter the first number :"))
        y=float(input("Enter the second number :"))
        print("Result is",exp(x,y))
    elif(choice==6):
        x=float(input("Enter the number :"))
        print("Result is",log(x))
    elif(choice==7):
        x=float(input("Enter the number :"))
        print("Result is",math.cos(math.radians(x)))
    elif(choice==8):
        x=float(input("Enter the number :"))
        print("Result is",math.sin(math.radians(x)))
    elif(choice==9):
        x=float(input("Enter the number :"))
        print("Result is",math.tan(math.radians(x)))
    elif(choice==10):
        break