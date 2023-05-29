import time
from game import Game
from colorama import Fore, Back, Style


def display_welcome_screen():
    """Displays the welcome screen to the player"""
    Game.clear()
    print(f'''



                         Welcome to

{Fore.LIGHTGREEN_EX}
    ███╗   ███╗██╗   ██╗    ██╗     ██╗████████╗████████╗██╗     ███████╗
    ████╗ ████║╚██╗ ██╔╝    ██║     ██║╚══██╔══╝╚══██╔══╝██║     ██╔════╝
    ██╔████╔██║ ╚████╔╝     ██║     ██║   ██║      ██║   ██║     █████╗
    ██║╚██╔╝██║  ╚██╔╝      ██║     ██║   ██║      ██║   ██║     ██╔══╝
    ██║ ╚═╝ ██║   ██║       ███████╗██║   ██║      ██║   ███████╗███████╗
    ╚═╝     ╚═╝   ╚═╝       ╚══════╝╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝

{Style.BRIGHT}
                    ███████╗███╗   ██╗███████╗██╗  ██╗
                    ██╔════╝████╗  ██║██╔════╝██║ ██╔╝
                    ███████╗██╔██╗ ██║█████╗  █████╔╝
                    ╚════██║██║╚██╗██║██╔══╝  ██╔═██╗
                    ███████║██║ ╚████║███████╗██║  ██╗
                    ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
{Style.RESET_ALL}

''')
    choice = input(f'''
    Do you want to start a
    {Fore.LIGHTGREEN_EX}N{Fore.RESET}EW GAME or
    {Fore.LIGHTGREEN_EX}C{Fore.RESET}ONTINUE an existing game

    or do you want to
    {Fore.LIGHTGREEN_EX}R{Fore.RESET}EAD the tutorial?\n\n
    ''').lower()
    return choice


def display_tutorial():
    """Displays the tutorial screen for the game"""
    Game.clear()
    print(f'''{Fore.LIGHTGREEN_EX}
    my little Snek


    The game is loosely based on the Tamagotchi pets of the last century.

    When you start a new game, you are asked for a name for your pet which
    should consist of 2 to 10 alphabetic characters. You then receive a unique
    ID for your pet, which you should write down if you want to continue
    playing at a later time. You can see this ID at any time during the game.

    Your pet ages over time. At certain intervals, there is a chance for your
    pet to either get hungry, poop or get sad. You can then take care of your
    pet by typing the starting letters of the functions to feed, clean or pet
    your pet to keep your pet healthy and happy.

    If you neglect your pet for too long and any 2 of the pet's needs go up to
    5, your pet will die and will be moved to the cemetery with all other
    deceased
    pets.
{Fore.RESET}
''')
    input(f'''
    Press {Fore.LIGHTGREEN_EX}ENTER{Fore.RESET} to get back to the main menu.
    ''')
    main()


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
    elif game_choice == 'r':
        display_tutorial()
    else:
        print('Invalid input.')
        time.sleep(1)
        game_choice = main()


main()
