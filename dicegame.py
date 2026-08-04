# # 31 07 2026

# # WAP to roll a dice and there are two players P1 and P2
# # initial start from P1 and there are two options roll and hold the dice when the both players 
# # rolls scores gets added only if number is 1 then score resets to zero and turn changes the 
# # player with higher score 20 wins but condition is
# # if the player holds the dice then the next player starts but score remains the same


import random
dice = random.randint(1,6)
print(dice)

def hold_dice():
    dice = 0
    return dice

def player_turn(player,score):
    while True:
        choice = input(f"{player}, roll or hold? ") 
        if choice == "roll":
            dice = roll_dice()
            print(f"You rolled a {dice}")
            score += dice
            print(f"{player}'s score: {score}")
        elif choice == "hold":
            print(f"{player}'s score: {score}")
            break
        else:
            print("Invalid choice. Please enter 'roll' or 'hold'.")
    return score
       
player1_score = 0
player2_score = 0

while True:
    player1_score = player_turn("Player 1", player1_score)
    if player1_score >= 20:
        print("Player 1 wins!")
        break
    player2_score = player_turn("Player 2", player2_score)
    if player2_score >= 20:
        print("Player 2 wins!")
        break


# import random

# def dice_game():
#     player1_score = 0
#     player2_score = 0

#     while True:
#         player1_score = player_turn("Player 1", player1_score)
#         if player1_score >= 20:
#             print("Player 1 wins!")
#             break
#         player2_score = player_turn("Player 2", player2_score)
#         if player2_score >= 20:
#             print("Player 2 wins!")
#             break

# dice_game()


