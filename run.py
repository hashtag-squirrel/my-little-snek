import time
import threading
import os
import sys
from colorama import Fore, Back, Style


class Pet:
    """
    Class to initialize any instance of Pet object.

    Attributes:
    name: Determined by user input, name of the pet
    type: Determines the type of pet, by default snake
    age, hunger, poop, sadness: By default 0 at moment of instantiation

    Methods:
    feed()
    clean()
    pet()
    get_hungry()
    defecate()
    get_sad()
    die()
    """
    def __init__(self, name, type='snake', age=0, hunger=0, poop=0, sadness=0,
                 dead=False):
        """Initializes the Pet"""
        self.type = type
        self.name = name
        self.age = age
        self.hunger = hunger
        self.poop = poop
        self.sadness = sadness
        self.dead = dead

    def __str__(self):
        """Returns the string interpretation of the object"""
        return f'''
        Type: {self.type.capitalize()}
        Name: {self.name}, Age: {self.age}
        Hunger: {self.hunger} | Poop: {self.poop} | Sadness: {self.sadness}
        '''

    def feed(self):
        """Reduces hunger"""
        print(f'Feeding {self.name}...')
        self.hunger -= 1

    def clean(self):
        """Reduces poop"""
        print('Cleaning poop...')
        self.poop -= 1

    def pet(self):
        """Reduces sadness"""
        print(f'Petting {self.name}...')
        self.sadness -= 1

    def get_hungry(self):
        """Increases hunger"""
        print(f'{self.name} gets hungry.')
        self.hunger += 1

    def defecate(self):
        """Increases poop"""
        print(f'{self.name} has pooped.')
        self.poop += 1

    def get_sad(self):
        """Increases sadness"""
        print(f'{self.name} is getting sad.')
        self.sadness += 1

    def die(self):
        """Checks properties and 'kills' the pet on certain conditions"""
        print(f'{self.name} has died of something. Game over.')

    def evaluate_properties(self):
        """Runs every tick and may increase hunger, poop or sadness"""
        print(f'Evaluating {self.name}...')

    def evaluate_lod(self):
        """Checks whether the pet is alive or dead and returns a boolean"""
        print(f'Checking if {self.name} is alive or dead...')
        if ((self.hunger == 5 and self.poop == 5)
            or (self.poop == 5 and self.sadness == 5)
                or (self.hunger == 5 and self.sadness == 5)):
            self.dead = True
            print('Bob is dead')
            return self.dead


def clear():
    """Clears the terminal window"""
    os.system('clear')


def display_welcome_screen():
    """Displays the welcome screen to the player"""
    clear()
    print('Welcome to My Little Snek\n')
    choice = input(f'''Do you want to start a
{Fore.LIGHTGREEN_EX}N{Fore.RESET}EW GAME or
{Fore.LIGHTGREEN_EX}C{Fore.RESET}ONTINUE an existing game?\n''').lower()
    return choice


def display_game(pet):
    """Displays the game"""
    time.sleep(1)
    clear()
    print(pet)
    print(f'''Do you want to
{Fore.LIGHTGREEN_EX}F{Fore.RESET}eed,
{Fore.LIGHTGREEN_EX}C{Fore.RESET}lean,
{Fore.LIGHTGREEN_EX}P{Fore.RESET}et or
{Fore.LIGHTGREEN_EX}Q{Fore.RESET}uit the game?\n''')


def get_input(pet):
    choice = input().lower()
    if choice == 'f':
        Pet.feed(pet)
    elif choice == 'c':
        Pet.clean(pet)
    elif choice == 'p':
        Pet.pet(pet)
    elif choice == 'q':
        print('Quitting game. Progress is saved. See you next time!')
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
        for character in '...\n':
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(1)
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


# def get_input():
#     name = input('Input your name\n')
#     print(f'Your name: {name}')
#     time.sleep(60)

main()
