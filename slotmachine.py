#
# Apple/Slots Attempt 1
#
print("Welcome to the Slot Machine Simulator")
print("To win the jackpot you need to have 3 cherries in a row.")
print("You can play up to 100 rounds at once. Select a number between 1 and 10")
games = input("How many games would you like to run?")
slotsPossible = ("apple", "apple", "apple", "cherry", "crown", "lemon")
from random import *
if int(games)<1 :
    print ("You didn't deserve to play anyway!")
if int(games)>100 :
    print ("Sorry you can only play 100 games so 100 is all you get!")
    games = 100
def play():
    slot1=choice (slotsPossible)
    slot2=choice (slotsPossible)
    slot3=choice (slotsPossible)
    win = ""
    if(slot1==slot2==slot3=="cherry"):
        win = "You're a big winner! Nice! $500!"
    if(slot1==slot2==slot3=="crown"):
        win = "You're kind of a winner... Woot? $100"
    if(slot1==slot2==slot3=="apple"):
        win = "You win an apple!"
    if(slot1==slot2==slot3=="lemon"):
        win = "Time to make some lemonade I guess."
    return slot1+":"+slot2+":"+slot3+" "+win
for i in range(int(games)) :
    print(play())
