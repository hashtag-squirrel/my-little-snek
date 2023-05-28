import random
import time
import emoji
from art import snake
from datahandler import Datahandler


class Pet:
    """
    Class to initialize any instance of Pet object.

    Attributes:
    name: Determined by user input, name of the pet
    id: Generated by Datahandler class on new game, used to load a pet in a
    continued game
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
    def __init__(
            self,
            id,
            name: str,
            birthdate,
            type='snake',
            age=0,
            hunger=0,
            poop=0,
            sadness=0,
            dead=False):
        """Initializes the Pet"""
        self.type = type
        self.name = name
        self.id = id
        self.birthdate = birthdate
        self.age = age
        self.hunger = hunger
        self.poop = poop
        self.sadness = sadness
        self.dead = dead
        self.snake_stage = 0

    def __str__(self):
        """Returns the string interpretation of the object"""
        return (f'''
        Name: {self.name.capitalize()} | Age: {self.age} | ID: {self.id}
{snake[self.snake_stage]}
                Hunger: {emoji.emojize(":mouse_face:") * self.hunger}''' +
                f'{" " * (6 - self.hunger)}' +
                f'| Poop: {emoji.emojize(":pile_of_poo:") * self.poop} ' +
                f'{" " * (6 - self.poop)}' +
                f'| Sadness: {emoji.emojize(":red_heart:") * self.sadness}')

    def feed(self):
        """Reduces hunger"""
        print(f'''
    Feeding {self.name}...''')
        if self.hunger > 0:
            self.hunger -= 1
            print(f'''
    {self.name} hisses happily!''')
        else:
            print(f'''
    {self.name} is not hungry right now.''')

    def clean(self):
        """Reduces poop"""
        print('''
    Cleaning poop...''')
        if self.poop > 0:
            self.poop -= 1
            print(f'''
    {self.name} slithers around on the cleaner floor.''')

    def pet(self):
        """Reduces sadness"""
        print(f'''
    Petting {self.name}...''')
        if self.sadness > 0:
            self.sadness -= 1
            print(f'''
    {self.name} smiles and hisses happily at you.''')

    def get_hungry(self):
        """Increases hunger"""
        if self.hunger < 5:
            self.hunger += 1

    def defecate(self):
        """Increases poop"""
        if self.poop < 5:
            self.poop += 1

    def get_sad(self):
        """Increases sadness"""
        if self.sadness < 5:
            self.sadness += 1

    def increase_age(self):
        """Increases age of the pet"""
        self.age += 1
        if self.age > 233:
            self.snake_stage = 4
        elif self.age > 89:
            self.snake_stage = 3
        elif self.age > 34:
            self.snake_stage = 2
        elif self.age > 8:
            self.snake_stage = 1
        elif self.age > 0:
            self.snake_stage = 0

    def die(self):
        """Checks properties and 'kills' the pet on certain conditions"""
        print(f'''
    {self.name} has died of neglect. Game over.''')
        deathtime = str(time.ctime())
        Datahandler.save_deceased_pet_to_file(self, deathtime)
        Datahandler.delete_pet_from_alive_file(self.id)

    def evaluate_properties(self):
        """Runs every tick and may increase hunger, poop or sadness"""
        chance = random.randint(1, 5)
        if chance <= 2:
            self.get_hungry()
        chance = random.randint(1, 5)
        if chance <= 2:
            self.defecate()
        chance = random.randint(1, 5)
        if chance <= 2:
            self.get_sad()

    def evaluate_lod(self):
        """Checks whether the pet is alive or dead and returns a boolean"""
        if ((self.hunger == 5 and self.poop == 5)
            or (self.poop == 5 and self.sadness == 5)
                or (self.hunger == 5 and self.sadness == 5)):
            self.dead = True
            self.die()
            return self.dead
