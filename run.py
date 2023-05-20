import time
import threading

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