print("\t\tWelcome to the Adventure Game")
print("It is a treasure hunt game where you need to choose the correct path to get the reward.")
one=input("You have two ways.Choose one between left and right :")
if one=='left':
    two=input("You now reached a river. Will you swim or use a boat :")
    if two=='swim':
        print('Unfortunately, you were eaten up by crocodiles.')
    elif two=='boat':
        print("You reached a man.He gives you 4 pills-red,yellow,blue,green.")
        three=input("You are asked to eat one of the pills, you choose :")
        if three=='red':
            print('You died of poison.')
        elif three=='green':
            print('You gain a lot of energy and become powerful.')
            four=input("You keep moving and find a forest.There are 4 weapons in the forest-sword,gun,bomb,knife. Choose one of them: ")
            if four=='sword':
                print("You chop your own arm unfortunately and die.")
            elif four=='gun':
                print("You take the gun and keep moving. A dragon approaches you.\nYou have only one bullet in your gun.")
                five=input("Will you hit the dragon on-head, neck,chest,arms: ")
                if five=='head':
                    print("Dragon was wearing a helmet, it blows fire at you and you die.")
                elif five=='neck':
                    print("The dragon dies. You keep moving. You are thirsty,you find a man offering water.")
                    six=input("He has a bottle, a mug , a bucket and a glass. Choose any one :")
                    if six=='bottle':
                        print("The water in the bottle was very poisonous and you die.")
                    elif six=='mug':
                        print("The water in the mug was muddy, your throat gets chocked and you die.")
                    elif six=='glass':
                        print("The glass was broken, you cut your fingers and start bleeding and you die.")
                    elif six=='bucket':
                        print("You have quenched your thirst successfully and you keep moving.")
                        seven=input("You finally find a key and 4 treasure boxes.Choose between 1,2,3,4 :")
                        if seven=='1':
                            print("The key oesn't work, you become frustrated and commit suicide.")
                        elif seven=='2':
                            print("The key successfully opens the box, but there was a corpse.You get scared and die.")
                        elif seven=='3':
                            print("The key successfully opens the treasure box.")
                            print("Congratulations! you have finally won the entire game and get a reward of $10000000.")
                        elif seven=='4':
                            print("The treasure box doesn't open, so you fire at it and the bullet strikes back at your head and you die.")
                        else:
                            print('Not a valid option. You lost.')  
                elif five=='chest':
                    print("The dragon was wearing a bullet-proof jacket,  it blows fire at you and you die.")
                elif five=='arms':
                    print("The dragon had extra arms,  it blows fire at you and you die.")
                else:
                    print('Not a valid option. You lost.')    
            elif four=='bomb':
                print("The bomb blasts and you're brutally killed.")
            elif four=='knife':
                print("You chop off your fingers unfortunately.")
        elif three=='yellow':
            print("You lose all youe energy in a moment and die.")
        elif three=='blue':
            print("You become unconscious.")
        else:
            print('Not a valid option. You lost.')
    else:
        print('Not a valid option. You lost.')
elif one=='right':
    print("You walked for 2 miles, didn't find anything and died.")
else:
    print('Not a valid option. You lost.')