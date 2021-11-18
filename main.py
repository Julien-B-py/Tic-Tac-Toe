from itertools import cycle
from os import system

from settings import SQUARES_INIT, SYMBOLS


def clear_console() -> None:
    """ Clear shell/terminal """
    system('cls')


def ask_player_to_play(player: str) -> None:
    """
    Ask the current player to make a move.
    Loop while the player is not making a valid move (e.g., sending incorrect string value, sending already used
    position)
    Parameters:
        player (str): Current player symbol: 'O' or 'X'
    """
    while True:
        answer = input(f'Player "{player}" turn. Which square number do you want to play (1-9) ?: ')
        # If the answer is valid and has not been played by someone already
        if answer in game_state.keys() and answer not in plays:
            # Update the grid with current player move
            game_state[answer] = player
            # Clear shell/terminal
            clear_console()
            # Update display
            display_board()
            # Add current player move to played moves list
            plays.append(answer)
            # Exit function
            return
        # If invalid answer or already played move
        else:
            print('Please check your entry.')


def display_board():
    """
    Display the current board state.
    """
    print(
        f'''
     |     |     
  {game_state['1']}  |  {game_state['2']}  |  {game_state['3']}  
_____|_____|_____
     |     |     
  {game_state['4']}  |  {game_state['5']}  |  {game_state['6']}  
_____|_____|_____
     |     |     
  {game_state['7']}  |  {game_state['8']}  |  {game_state['9']}  
     |     |     
    '''
    )


def is_draw() -> bool:
    """
    Check if the board is completely filled.
    Returns:
        status (bool): Returns True if the board is filled.
    """
    # Loop through all game_state dictionary values
    for value in game_state.values():
        # If any value is from integer type, game is still playable if nobody won already
        if isinstance(value, int):
            return False
    print('Draw!')
    return True


def is_there_a_winner(player: str) -> bool:
    """
    Check all possibilities to see if a player won the game.
    Parameters:
        player (str): Current player symbol: 'O' or 'X'
    Returns:
        status (bool): Returns True if a player has actually won.
    """
    # Checking if any column is completed
    for i in range(1, 4):
        if game_state[str(i)] == game_state[str(i + 3)] == game_state[str(i + 6)]:
            print(f'Player "{player}" wins.')
            return True

    # Checking if any row is completed
    for i in range(2):
        if game_state[str(1 + i * 3)] == game_state[str(2 + i * 3)] == game_state[str(3 + i * 3)]:
            print(f'Player "{player}" wins.')
            return True

    # Checking if any diagonal is completed
    if game_state['1'] == game_state['5'] == game_state['9'] or game_state['3'] == game_state['5'] == game_state['7']:
        print(f'Player "{player}" wins.')
        return True

    return False


def reset_game() -> bool:
    """
    Ask players if they want to start another game.
    Returns:
        answer (bool): Returns True if any player answered 'y'
    """
    answer = input('Another game? (Y/N): ').lower()
    return answer == 'y'


if __name__ == '__main__':

    game_over = False

    # Main loop
    while not game_over:

        # Create a copy of SQUARES_INIT to store the game state
        game_state = dict(SQUARES_INIT)
        # Change players starting order everytime they play another game
        SYMBOLS = SYMBOLS[::-1]
        # Reset or initialize the list of played moves
        plays = []
        display_board()

        # Infinite loop through players symbols list using itertools.cycle
        for symbol in cycle(SYMBOLS):
            current_player = symbol
            # Make a move
            ask_player_to_play(current_player)
            # Check if the current game is over
            if is_there_a_winner(current_player) or is_draw():
                # Check if players wants to rematch. If not exit while loop.
                if not reset_game():
                    # Exit main loop
                    game_over = True
                # If players want to play again exit for loop so the while loop can restart from beginning
                break
        # Clear shell/terminal
        clear_console()
