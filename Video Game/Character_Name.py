import time
def character_name():
    print("Now, choose a name.")
    player_name = input().title()
    time.sleep(1)

    print(f"Welcome to your adventure, {player_name}.")
    time.sleep(1)
    return player_name

if __name__ == '__main__':
    print("hello")