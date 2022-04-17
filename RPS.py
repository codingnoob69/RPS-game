#making rock paper scissors
import random

while True:
    print("Rock beats scissors, paper beats rock, scissors beats paper")
    print("rock = 1, paper = 2, scissors = 3")

    choice = int(input("User turn: "))
    #takes input from user

    if choice == 1:
        pick = 'rock'
    if choice == 2:
        pick = 'paper'
    if choice == 3:
        pick = 'scissors'
    #loops different picks

    print("User choice is " +pick)
    print("Now it's comp turn...........")

    comp_pick = random.randint(1, 3)
    #comp picks number 1,2 or 3

    if comp_pick == 1:
        pick2 = 'rock'
    if comp_pick == 2:
        pick2 = 'paper'
    if comp_pick == 3:
        pick2 = 'scissors'
    #computers pick

    print("comp choice is " +pick2)

    if(choice == comp_pick):
        result = "tie"
    if(choice == 1 and comp_pick == 2)or(choice == 2 and comp_pick == 1):
        result = "paper"
    if(choice == 2 and comp_pick == 3)or(choice == 3 and comp_pick == 2):
        result = "scissors"
    if(choice == 1 and comp_pick == 3)or(choice == 3 and comp_pick == 1):
        result = "rock"
    #prints result of choices in the game

    # Printing either user or computer wins
    if result == pick:
        print("You win...    :)")
    elif result == "tie":
        print("TIE")
    else:
        print("You lose...   :(")

    print("Do you wanna pla again(Y/N)??")
    ans = input()

    if ans == 'N' or ans == 'n':
        break
