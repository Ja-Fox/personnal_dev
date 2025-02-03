import random
import time

def defense_against_monster(player_character, current_player_health):
    print("The monster attacks you!")
    monster_hit = random.randint(10,20)
    damage_to_player = random.randint (10,25)

    chance_to_evade = player_character.chance_to_evade()
    chance_to_defend = player_character.defense_against_attack()

    time.sleep(1)

    if chance_to_evade >= monster_hit:
        damage_to_player = 0
        print ("You evaded the attack and take 0 damage!")

    else:
        print("The monster's attack connects!")
        time.sleep(2)

        if chance_to_defend <= 1:
            damage_to_player = 1000000
            print(f"Your defense critically fails. You are mortally wounded.")
            time.sleep(2)

        elif chance_to_defend >= 20:
            damage_to_player = 0
            print (f"You shielded yourself and take no damage!")
            time.sleep(1)

        elif chance_to_defend >= damage_to_player:
            damage_to_player = damage_to_player // 5
            print (f"You take {damage_to_player} damage!")
            time.sleep(1)

        elif chance_to_defend < damage_to_player:
            damage_to_player = damage_to_player - chance_to_defend
            print(f"The beast strikes you for {damage_to_player} damage.")
            time.sleep(1)
        

    player_health_after_defense = current_player_health - damage_to_player
    return player_health_after_defense