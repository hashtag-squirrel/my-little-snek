import time
import threading
import os
import sys
import random
from pet import Pet
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


def display_game(pet):
    """Displays the game"""
    time.sleep(1)
    Game.clear()
    print(pet)
    print(f'''Do you want to
{Fore.LIGHTGREEN_EX}F{Fore.RESET}eed,
{Fore.LIGHTGREEN_EX}C{Fore.RESET}lean,
{Fore.LIGHTGREEN_EX}P{Fore.RESET}et or
{Fore.LIGHTGREEN_EX}Q{Fore.RESET}uit the game?\n''')


def get_input(pet):
    while True:
        if pet.evaluate_lod():
            break
        choice = input().lower()
        if choice == 'f':
            pet.feed()
            display_game(pet)
        elif choice == 'c':
            pet.clean()
            display_game(pet)
        elif choice == 'p':
            pet.pet()
            display_game(pet)
        elif choice == 'q':
            quit_game()
        else:
            print('invalid input')


def start_new_game():
    """Starts a new game"""
    print('Starting new game...')
    name = input('Name your pet:\n').capitalize()
    my_pet = Pet(name)
    tick_thread = threading.Thread(target=tick_time, args=(my_pet,))
    tick_thread.start()
    input_thread = threading.Thread(target=get_input, args=(my_pet,))
    input_thread.start()
    return my_pet


def quit_game():
    """Quits the current game, closes all threads"""
    print('Quitting game. Progress is saved. See you next time!')


def tick_time(pet):
    """Function that 'ticks' at certain intervals,
    runs in parallel to main thread
    Calls Pet methods:
    evaluate_properties()
    evaluate_lod()

    Calls game methods:
    save_game()
    """
    while True:
        # for character in '...\n':
        #     sys.stdout.write(character)
        #     sys.stdout.flush()
        #     time.sleep(1)
        time.sleep(10)
        pet.increase_age()
        pet.evaluate_properties()
        if pet.evaluate_lod():
            break
        display_game(pet)


def main():
    """Main function for the game"""
    game_choice = display_welcome_screen()
    if game_choice == 'n':
        my_pet = start_new_game()
        display_game(my_pet)
    else:
        game_choice = display_welcome_screen()


main()
