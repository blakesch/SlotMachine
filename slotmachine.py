#
# Apple/Slots Attempt 1
#
print("Welcome to the Slot Machine Simulator")
print("To win the jackpot you need to have 3 cherries in a row.")
print("You can play up to 100 rounds at once. Select a number between 1 and 100")
games = input("How many games would you like to run?")
slotsPossible = ("apple", "apple", "apple", "cherry", "crown", "lemon")
from random import *
if int(games)<1 :
    print ("You didn't deserve to play anyway!")
if int(games)>100 :
    print ("Sorry you can only play 100 games so 100 is all you get!")
    games = 10025
def play():
    slot1=choice (slotsPossible)
    slot2=choice (slotsPossible)
    slot3=choice (slotsPossible)
    win = ""
    if(slot1==slot2==slot3=="cherry"):
        win = "\n\nYou're a big winner! Nice! $500!\n"
    if(slot1==slot2==slot3=="crown"):
        win = "\n\nYou're kind of a winner... Woot? $100\n"
    if(slot1==slot2==slot3=="apple"):
        win = "\n\nYou win an apple!\n"
    if(slot1==slot2==slot3=="lemon"):
        win = "\n\nTime to make some lemonade I guess.\n"
    return slot1+":"+slot2+":"+slot3+" "+win
for i in range(int(games)) :
    print(play())
