from game import Game
from colorama import Fore, Back, Style


def display_welcome_screen():
    """Displays the welcome screen to the player"""
    # Game.clear()
    print('Welcome to My Little Snek\n')
    choice = input(f'''Do you want to start a
{Fore.LIGHTGREEN_EX}N{Fore.RESET}EW GAME or
{Fore.LIGHTGREEN_EX}C{Fore.RESET}ONTINUE an existing game?\n''').lower()
    return choice


def main():
    """Main function for the game"""
    game_choice = display_welcome_screen()
    if game_choice == 'n':
        my_game = Game()
        my_game.start_new_game()
        my_game.display_game()
    elif game_choice == 'c':
        my_game = Game()
        my_game.load_game()
        my_game.display_game()
    else:
        game_choice = display_welcome_screen()


main()
