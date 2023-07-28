# This is just a very basic robot speaker that use computer's text to speech tool using python os package
import os

# This is the main entry point
if __name__ == '__main__':
    print("Welcome to Robo Speaker!")
    while True:
        x = input("enter the sentence to say: ")
        if (x == 'bye'):
            break
        command = f"say {x}"
        os.system(command)
