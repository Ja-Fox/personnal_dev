import time
import random

def Locations():
    villages = ['Spirewood','Martlock','Willowfen','Ravenwatch',"Burrough's Crossing"]
    choice = random.choice(villages)
    villages.remove(choice)
    return choice


def Quest_Text(boss,player_name):
    text = f"""Welcome to the world of Averfell. In this harsh land a {boss} has emerged
from the shadows to terrorize the people. Its malevolence knows no bounds, and the villagers
live in constant dread.......

The town mayor looks to you for help, a last hope at saving his people from evil.

"Please, {player_name}, hunt down this abomination. Rid this world of that curse. I will mark your
map of with area that the beast hunts from...unfortunately we do not know its exact location." """
    for character in text:
        if character == ' ':
            time.sleep(.05)
        print (character,end='',flush=True)
        time.sleep(.05)


def Starting_Village():
    start = Locations()
    text = f"""You stand at the gates of {start}, a population center in Averfell. May the fates be on your side."""
    for character in text:
        if character == ' ':
            time.sleep(.05)
        print (character,end='',flush=True)
        time.sleep(.05)
    return start


