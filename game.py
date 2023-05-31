import art
from pet import Pet
from datahandler import Datahandler
import threading
import time
import os
from colorama import Fore, Back, Style


class Game:
    """Class that controls every functionality around the game,
    instantiates the running game object
    """
    def __init__(self):
        self._is_ticking = False
        pass

    def clear():
        """Clears the terminal window"""
        os.system('clear')

    def display_welcome_screen():
        """Displays the welcome screen to the player"""
        Game.clear()
        print(art.welcome)
        choice = input(f'''
        Do you want to start a
        {Fore.LIGHTGREEN_EX}N{Fore.RESET}EW GAME or
        {Fore.LIGHTGREEN_EX}C{Fore.RESET}ONTINUE an existing game

        or do you want to
        {Fore.LIGHTGREEN_EX}R{Fore.RESET}EAD the tutorial?\n\n
        ''').lower()
        return choice

    def display_game(self):
        """Displays the game"""
        time.sleep(1)
        Game.clear()
        print(self.my_pet)
        print(f'''
    Do you want to
    {Fore.LIGHTGREEN_EX}F{Fore.RESET}eed,
    {Fore.LIGHTGREEN_EX}C{Fore.RESET}lean,
    {Fore.LIGHTGREEN_EX}P{Fore.RESET}et or
    {Fore.LIGHTGREEN_EX}Q{Fore.RESET}uit the game?\n''')

    def save_game(self, game, pet):
        """Method to save the current running game,
        should be called every 10 ticks
        Calls Datahandler methods
        """
        print(f'Saving game...')
        if game == 'new':
            Datahandler.save_new_pet_to_file(pet)
        elif game == 'save':
            Datahandler.save_pet_to_file(pet)

    def _tick_time(self, pet):
        """Function that 'ticks' at certain intervals,
        runs in parallel to main thread
        Calls Pet methods:
        evaluate_properties()
        evaluate_lod()

        Calls game methods:
        save_game()
        """
        while self._is_ticking is True:
            if pet.evaluate_lod():
                break
            time.sleep(10)
            pet.increase_age()
            pet.evaluate_properties()
            self.display_game()
            if pet.age % 5 == 0:
                self.save_game('save', pet)

    def _get_input(self, pet):
        """Function that waits for input as long as the game runs"""
        while self._is_ticking is True:
            if pet.evaluate_lod():
                break
            choice = input().lower()
            if choice == 'f':
                pet.feed()
                self.display_game()
            elif choice == 'c':
                pet.clean()
                self.display_game()
            elif choice == 'p':
                pet.pet()
                self.display_game()
            elif choice == 'q':
                self.quit_game()
                break
            else:
                print('invalid input')

    def start_new_game(self):
        """Starts a new game"""
        print('Starting new game...')
        while True:
            name = input('Name your pet:\n').capitalize()
            if self.validate_name(name):
                break
        id = Datahandler.generate_id()
        birthdate = str(time.ctime())
        self.my_pet = Pet(id, name, birthdate)
        self.save_game('new', self.my_pet)
        self._is_ticking = True
        self.tick_thread = threading.Thread(
            target=self._tick_time,
            args=(self.my_pet,))
        self.tick_thread.start()
        self.input_thread = threading.Thread(
            target=self._get_input,
            args=(self.my_pet,))
        self.input_thread.start()

    def validate_id(self, id):
        """Validates input id for correct format of 6 digit number string"""
        try:
            [int(digit) for digit in id]
            if len(id) != 6:
                raise ValueError(
                    f'Exactly 6 digits required, you provided {len(id)}'
                    )
        except ValueError as e:
            print(f'Invalid data: {e}, please try again.\n')
            return False
        else:
            return True

    def validate_name(self, name):
        """Validates name input to use a name between 2 and 10 characters
        which are all alphabetic
        """
        try:
            if not name.isalpha():
                raise TypeError
            if len(name) < 2 or len(name) > 10:
                raise ValueError
        except TypeError:
            print(f'''
    Invalid input: {name}.
    Please try again with only alphabetic characters.''')
            return False
        except ValueError:
            print(f'''
    Invalid input, you entered {len(name)} characters.
    The name should consist of 2-10 characters.''')
            return False
        else:
            return True

    def quit_game(self):
        """Quits the current game, closes all threads"""
        print('''
    Quitting game. Wait until saving is done...''')
        self._is_ticking = False
        time.sleep(10)
        self.save_game('save', self.my_pet)
        print(f"""
    Don't forget to write down your pet's ID if you want to come back!
    The ID is {Fore.LIGHTGREEN_EX}{self.my_pet.id}{Fore.RESET}.

    See you next time!
    """)
        del self

    def load_game(self):
        """Method to initialize new game with existing data"""
        print('Loading game...')
        while True:
            id = input("Please enter your pet's ID (6 digits):\n")
            if self.validate_id(id):
                if Datahandler.check_if_id_exists(id):
                    break
        # Getting and preparing pet data from file
        pet = Datahandler.get_pet_from_file(id)
        name = pet[1]
        type = pet[2]
        age = int(pet[3])
        hunger = int(pet[4])
        poop = int(pet[5])
        sadness = int(pet[6])
        birthdate = pet[7]
        # Instantiating Pet object
        self.my_pet = Pet(
            id,
            name,
            birthdate,
            type,
            age,
            hunger,
            poop,
            sadness)
        # Starting game threads
        self._is_ticking = True
        self.tick_thread = threading.Thread(
            target=self._tick_time,
            args=(self.my_pet,))
        self.tick_thread.start()
        self.input_thread = threading.Thread(
            target=self._get_input,
            args=(self.my_pet,))
        self.input_thread.start()
