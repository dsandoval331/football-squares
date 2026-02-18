import pandas as pd
import random

def create_football_squares_board(players):
    """
    Creates a 10x10 football squares board, assigns players to squares,
    and assigns random numbers (0-9) to the axes.

    Args:
        players (list): A list of player names.

    Returns:
        pandas.DataFrame: The completed football squares board.
    """
    if not players:
        print("Error: No players provided.")
        return None

    # 1. Create a 10x10 empty grid
    board = pd.DataFrame(index=range(10), columns=range(10))

    # 2. Distribute squares among players
    total_squares = 100
    num_players = len(players)
    squares_per_player = total_squares // num_players
    remaining_squares = total_squares % num_players

    assigned_squares = []
    for player in players:
        assigned_squares.extend([player] * squares_per_player)
    # Distribute any remaining squares to the first few players
    assigned_squares.extend([players[i] for i in range(remaining_squares)])
    
    # Shuffle the assigned squares to randomize placement
    random.shuffle(assigned_squares)

    # Fill the board with assigned players
    for i in range(10):
        for j in range(10):
            board.iloc[i, j] = assigned_squares.pop(0)

    # 3. Assign random numbers (0-9) to rows and columns
    # The actual "game" part requires the final score digits
    home_team_numbers = random.sample(range(10), 10)
    away_team_numbers = random.sample(range(10), 10)

    board.index = away_team_numbers
    board.columns = home_team_numbers
    
    # Add team labels for clarity
    board.index.name = "Away Team (e.g., 49ers) Score Last Digit"
    board.columns.name = "Home Team (e.g., Chiefs) Score Last Digit"

    return board

# --- Example Usage ---
player_list = ["Danny", "Rob", "Tom", "James", "Joe", "Anthony", "Hunt", "Tito", "Lira", "Joday"]

# Ensure you have pandas installed (pip install pandas)
game_board = create_football_squares_board(player_list)

if game_board is not None:
    print("--- Football Squares Board ---")
    # You can print the board or save it to a CSV file
    print(game_board)
    
    # To save to a CSV file (requires pandas)
    # game_board.to_csv("football_squares_board.csv")
    print("\nBoard created successfully.")