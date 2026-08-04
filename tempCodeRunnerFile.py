def dice_game():
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

dice_game()