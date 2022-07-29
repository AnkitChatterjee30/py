import random

print("Press 1 for Stone")
print("Press 2 for Paper")
print("Press 3 for Scissors \n")

game_count=0
your_score=0
comp_score=0
while (game_count<=5):
    your_choice=int(input("Enter a number between between 1,2,3 :"))
    if(your_choice==1):
        print("You chose Stone.\n")
    elif(your_choice==2):
        print("You chose Paper.\n")
    elif(your_choice==3):
        print("You chose Scissors.\n")
    comp_choice=random.randint(1,3)

    if(comp_choice==1):
        print("Computer chose Stone.\n")
    elif(comp_choice==2):
        print("Computer chose Paper.\n")
    elif(comp_choice==3):
        print("Computer chose Scissors.\n")


    if(your_choice==comp_choice):
        game_count+=1
        print("Match Drawn !")
        print("Your score is ",your_score)
        print("Computer's score is",comp_score)
        print("Matches played till now is",game_count)
        
    elif(your_choice==1 and comp_choice==3)or(your_choice==2 and comp_choice==1)or(your_choice==3 and comp_choice==2):
        game_count+=1
        your_score+=1
        print("You won the match.")
        print("Your score is ",your_score)
        print("Computer's score is",comp_score)
        print("Matches played till now is",game_count)

    elif(your_choice==1 and comp_choice==2)or(your_choice==2 and comp_choice==3)or(your_choice==3 and comp_choice==1):
        comp_score+=1
        game_count+=1
        print("You have lost the match.")
        print("Your score is ",your_score)
        print("Computer's score is",comp_score)
        print("Matches played till now is",game_count)

    elif(your_choice>3 or your_choice<1):
        print("Invalid Option\n")
    if(game_count==5) and (your_score==comp_score):
        print("The Tournament ended up in a Tie.\n")
        break
    elif(game_count==5) and (your_score<comp_score):
        print("You've lost the tournament.\n")
        break
    elif(game_count==5) and (your_score>comp_score):
        print("You've won the tournament.\n")
        break
    
