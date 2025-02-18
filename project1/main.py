import random

computer=random.choice([-1,0,1])
yourSR=input("Enter Your Choice :")
yourDict={"w":-1,"g":0,"s":1}
reveseDict={-1:"w",0:"g",1:"s"}

you=yourDict[yourSR]

print(f"You chose {reveseDict[you]}\ncomputer chose {reveseDict[computer]}")

if(computer == you):
    print("Its A Draw !")
else:
    if(computer == -1 and you == 1):
        print("You Win!")
    elif(computer == -1 and you == 0):
        print("You Lose!")
    elif(computer == 1 and you == -1):
        print("You Lose!")
    elif(computer == 1 and you == 0):
        print("You Win!")
    elif(computer == 0 and you == -1):
        print("You Win!")
    elif(computer == 0 and you == 1):
        print("You Lose!")
    else:
        print("Something Wrong!")