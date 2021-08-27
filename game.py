import time
import os
import random

os.system("clear")
print("Hello")

time.sleep(2)

print("Welcome to the game rock-paper-scissors")

time.sleep(3)

os.system("clear")



def result(comp_move,ur_move):
    print("\vComputer's move : {} \nYour move : {}".format(comp_move,ur_move))



def match():
    moves = {1:"r", 2: "p", 3:"s"}

    rnd = random.randint(1,3)

    ur_move = input("Enter 'r', 'p' or 's'\n")

    ur_move = ur_move.lower()

    comp_move = moves.get(rnd)

    if(comp_move == ur_move):
        print("\nMatch Drawn.")
        result(comp_move,ur_move)

    elif(comp_move == 'r' and ur_move == 'p'):
        print("\nYou win!!")
        result(comp_move,ur_move)

    elif(comp_move == 'p' and ur_move == 'r'):
        print("\nYou Lose!!")
        result(comp_move,ur_move)

    elif(comp_move == 'p' and ur_move == 's'):
        print("\nYou Win!!")
        result(comp_move,ur_move)

    elif(comp_move == 's' and ur_move == 'p'):
        print("\nYou Lose!!")
        result(comp_move,ur_move)

    elif(comp_move == 's' and ur_move == 'r'):
        print("\nYou Win!!")
        result(comp_move,ur_move)

    elif(comp_move == 'r' and ur_move == 's'):
        print("\nYou Lose!!")
        result(comp_move,ur_move)

    else: 
        print("Wrong response!!!")

def end_credits():
    thanks = 'Thanks For Playing !!'
    thanks.upper()
    for i in thanks:
        print(i, end= " ")
        time.sleep(0.1)

print('\n')



start = 'y'

while(start == 'y'):
    match()
    print("Do you want to continue playing? (y/n)")
    start = input()


time.sleep(2)
os.system("clear")
end_credits()
time.sleep(2)
print("\nBye..")
