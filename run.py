import time
import threading
import os
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
        {self.type}
        {self.name}{self.age}
        {self.hunger}{self.poop}{self.sadness}
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
{Fore.LIGHTGREEN_EX}C{Fore.RESET}ONTINUE an existing game?\n''')
    return choice

# def get_input():
#     name = input('Input your name\n')
#     print(f'Your name: {name}')


def main():
    """Main function for the game"""
    display_welcome_screen()
    # time.sleep(60)


thread1 = threading.Thread(target=main)
# thread2 = threading.Thread(target=get_input)

thread1.start()
# thread2.start()
