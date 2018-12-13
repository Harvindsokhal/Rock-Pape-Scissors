from random import randint


t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
 
player = False
 
while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
        print()
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            print()
        else:
            print("You win!", player, "smashes", computer)
            print()
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            print()
        else:
            print("You win!", player, "covers", computer)
            print()
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            print()
        else:
            print("You win!", player, "cut", computer)
            print()
    else:
        print("That's not a valid option. Check your spelling!")
    player = False
    computer = t[randint(0,2)]
