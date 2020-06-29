from random import randint


t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0, 2)]
player = True

while player == True:
    player = input("Rock, Paper, Scissors?  :")
    if player == computer:
        print("It's a Tie")
    elif player == "Rock" or "rock":
        if computer == "Paper":
            print("You lose!  " + computer + "  covers  " + player)
        else:
            print("You win!  " + player + "  smashes  " + computer)
    elif player == "Paper" or "paper":
        if computer == "Scissors":
            print("You lose!  " + computer + "  cut  " + player)
        else:
            print("You win!  " + player + "  covers  " + computer)
    elif player == "Scissors" or "scissors":
        if computer == "Rock":
            print("You lose!  " + computer + "  smashes  " + player)
        else:
            print("You win!  " + player + "  cut  " + computer)
    else:
        print("It is not a valid play. Check your spelling")


