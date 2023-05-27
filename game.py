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
        pass

    def clear(self):
        """Clears the terminal window"""
        os.system('clear')

    def display_game(self):
        """Displays the game"""
        time.sleep(1)
        self.clear()
        print(self.my_pet)
        print(f'''Do you want to
{Fore.LIGHTGREEN_EX}F{Fore.RESET}eed,
{Fore.LIGHTGREEN_EX}C{Fore.RESET}lean,
{Fore.LIGHTGREEN_EX}P{Fore.RESET}et or
{Fore.LIGHTGREEN_EX}Q{Fore.RESET}uit the game?\n''')

    def _tick_time(self, pet):
        """Function that 'ticks' at certain intervals,
        runs in parallel to main thread
        Calls Pet methods:
        evaluate_properties()
        evaluate_lod()

        Calls Datahandler methods:
        save_pet_to_file()
        """
        while True:
            if pet.evaluate_lod():
                break
            time.sleep(10)
            pet.increase_age()
            pet.evaluate_properties()
            self.display_game()
            if pet.age % 10 == 0:
                Datahandler.save_pet_to_file(pet)

    def _get_input(self, pet):
        while True:
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
            else:
                print('invalid input')

    def start_new_game(self):
        """Starts a new game"""
        print('Starting new game...')
        name = input('Name your pet:\n').capitalize()
        id = Datahandler.generate_id()
        self.my_pet = Pet(name, id)
        Datahandler.save_new_pet_to_file(self.my_pet)
        tick_thread = threading.Thread(target=self._tick_time,
                                       args=(self.my_pet,))
        tick_thread.start()
        input_thread = threading.Thread(target=self._get_input,
                                        args=(self.my_pet,))
        input_thread.start()

    def quit_game(self):
        """Quits the current game, closes all threads"""
        print('Quitting game. Progress is saved. See you next time!')

    def save_game(self):
        """Method to save the current running game,
        should be called every tick
        """
        print(f'Saving game...')

    def load_game(self):
        """Method to initialize new game with existing data"""
        print('Starting new game...')
        # self.my_pet = Pet(name)
        # tick_thread = threading.Thread(target=self._tick_time,
        #                                args=(self.my_pet,))
        # tick_thread.start()
        # input_thread = threading.Thread(target=self._get_input,
        #                                 args=(self.my_pet,))
        # input_thread.start()
