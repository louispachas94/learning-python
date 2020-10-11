import random

print('Welcome ! What is your name ')
name=input()
print(name +' would you like to play a number guessing game ')
game_choice=input()

if game_choice in ('yes','sure','ok'):
    print ("let's start")

elif game_choice in ('no','nope','na'):
    exit()
