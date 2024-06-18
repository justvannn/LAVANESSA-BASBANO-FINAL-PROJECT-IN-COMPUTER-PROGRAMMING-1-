print("Number 6.")
def roll_dice():
    return random.randint(1, 6)

def play_best_of_three():
    player1_wins = 0
    player2_wins = 0
    
    while player1_wins < 2 and player2_wins < 2:
        print("\nRound Start!")
        
        input(f"Player 1, press Enter to roll the dice...")
        player1_roll = roll_dice()
        print(f"Player 1 rolled: {player1_roll}")
    
        input(f"Player 2, press Enter to roll the dice...")
        player2_roll = roll_dice()
        print(f"Player 2 rolled: {player2_roll}")
        
        if player1_roll > player2_roll:
            print("Player 1 wins this round!")
            player1_wins += 1
        elif player2_roll > player1_roll:
            print("Player 2 wins this round!")
            player2_wins += 1
        else:
            print("It's a tie this round!")
        
        print(f"Score: Player 1 - {player1_wins}, Player 2 - {player2_wins}")
    
    if player1_wins == 2:
        print("\nPlayer 1 wins the game!")
    else:
        print("\nPlayer 2 wins the game!")


