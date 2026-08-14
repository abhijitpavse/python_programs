# 04 08 2026

# using functions 

import random
def UpdateScoreAndPlayer(score1,score2,player,dice):
    if choice != 1:
        if player == 1:
            score1 += dice
        else:
            score2 += dice

    else:
        if player == 1:
            player = 2
            score1 = 0
        else:
            player = 1
            score2 = 0

    return score1,score2,player


def hold(player):
    if player == 1: 
        player = 2
    else:
        player = 1
    return player

score1 = 0
score2 = 0
player = 1

while score1 < 20 and score2 < 20:
    print("1.Roll \n 2.Hold")
    choice = input("Enter your choice: ")

    if choice == '1':
        dice = random.randint(1,6)

        score1,score2,player = UpdateScoreAndPlayer(score1,score2,player,dice)
        print("Current Player: ",player)
        print(f"Player 1 Score: {score1}")
        print(f"Player 2 Score: {score2}")

    elif (choice == '2'):
        player = hold(player)
        print("Current Player: ",player)


if score1 >= 20:
    print ("Player 1 Wins!")
else:
    print ("Player 2 Wins!")
   