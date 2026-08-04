# # WAP to roll a dice and there are two players P1 and P2
# # initial start from P1 and there are two options roll and hold the dice when the both players 
# # rolls scores gets added only if number is 1 then score resets to zero and turn changes the 
# # player with higher score 20 wins but condition is
# # if the player holds the dice then the next player starts but score remains the same

import random 

player =1

player1=0
player2=0

while player1<20 and player2<20:
    if player==1:
        choice = input("1.Roll \n 2.Hold")

        if choice == '1':
            dice = random.randint(1,6)
            print("Dice:",dice)

            if dice != 1:
                player1 += dice
                print("Player 1 score:",player1)

            else:
                player1 = 0
                print("player1 score reset to 0:")
                print("player1 score",player1)
                player = 2
            
        elif choice == '2':
            player = 2
            print("player1 score:",player1)

    elif player == 2:
        choice = input("1.Roll: \n 2.Hold:")

        if choice == '1':
            dice = random.randint(1,6)
            print("Dice:",dice)

            if dice != 1:
                player2 += dice
                print("Player 2 score:",player2)

            else:
                player2 = 0
                print("player2 score reset to 0")
                print("player2 score",player2)
                player = 1

        elif choice == '2':
            player = 1
            print("player2 score:",player2)

if player1 >= 20:
    print("Player 1 wins!")
else:
    print("Player 2 wins!")