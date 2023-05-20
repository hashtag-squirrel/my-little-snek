import time
import threading

class Pet:
    """
    Class to initialize any instance of Pet object.

    Attributes: 
    name: Determined by user input, name of the pet
    type: Determines the type of pet, by default snake
    age, hunger, poop, sadness: By default 0 at moment of instantiation
    """
    def __init__(self, name, type='snake', age=0, hunger=0, poop=0,sadness=0):
        """Initializes the Pet"""
        self.type = type
        self.name = name
        self.age = age
        self.hunger = hunger
        self.poop = poop
        self.sadness = sadness
    
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
    
    def clean(self):
        """Reduces poop"""
        print('Cleaning poop...')
    
    def pet(self):
        """Reduces sadness"""
        print(f'Petting {self.name}...')
    
    def die(self):
        """Checks properties and 'kills' the pet on certain conditions"""
        print(f'{self.name} has died of something. Game over.')

def get_input():
    name = input('Input your name\n')
    print(f'Your name: {name}')

def main():
    print('Welcome to My Little Snek')
    t = time.time()
    print(time.ctime())
    time.sleep(5)
    print(f'It is now {time.ctime()}. {round(time.time()-t)} seconds have passed.')

thread1 = threading.Thread(target=main)
thread2 = threading.Thread(target=get_input)

thread1.start()
thread2.start()