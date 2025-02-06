def movement_choice():
    cardinal_directions = ['north','south','east','west']
    print("Your options are North, South, East, or West.")
    player_movement_direction = input("What direction will you move? ").lower()
    while player_movement_direction:
        if player_movement_direction.isdigit():
            print("You must enter a direction to travel.")
            player_movement_direction = input("What direction will you move? ").lower()
            
        elif player_movement_direction not in cardinal_directions:
            print("Invalid direction.")
            player_movement_direction = input("What direction will you move? ").lower()

        else:
            return player_movement_direction


def movement_execution(player_movement_direction, player_location):
        if player_movement_direction == 'north':
            player_location['y'] += 1

        if player_movement_direction == 'south':
            player_location['y'] -= 1

        if player_movement_direction == 'east':
            player_location['x'] += 1

        if player_movement_direction == 'west':
            player_location['x'] -= 1


        return player_location













# def Move(player_location):
#     cardinal_directions = ['north','south','east','west']
#     print("Your options are North, South, East, or West.")
#     time.sleep(1)
#     player_movement_direction = input("What direction will you move? ").lower()
#     while True:
#         if player_movement_direction.isdigit():
#             print("Invalid direction.")
#             continue
#             # player_movement_direction = input("What direction will you move? ").lower()

#         elif player_movement_direction not in cardinal_directions:
#             print("Invalid direction.")
#             continue
#             # player_movement_direction = input("What direction will you move? ").lower()

#         else:
#             player_movement_distance = int(input("How many steps? "))

#         if player_movement_direction == 'north':
#             player_location['x'] += player_movement_distance

#         if player_movement_direction == 'south':
#             player_location['x'] -= player_movement_distance

#         if player_movement_direction == 'east':
#             player_location['y'] += player_movement_distance

#         if player_movement_direction == 'west':
#             player_location['y'] -= player_movement_distance


#         return player_location


        # if direction == 'north':
        #         encounter = random.randint(1,15)
        #         if distance >= encounter:
        #             distance = encounter
        #             steps_n += distance
        #             print(f"You only moved {distance} steps before encoutering a monster to fight!")
        #             if steps_n < 15:
        #                 Combat_Sequence.easy_combat(health,player_character,player_items)
        #                 time.sleep(2)
        #                 found_potion = Loot_Generator.beginner_potion_generator()
        #                 if found_potion:
        #                     player_items.append(found_potion)
        #                 else:
        #                     continue























#################################################################################
#################################################################################
#################################################################################


#         # time.sleep(1.5)
#         # print(f"You moved {distance} steps {direction}")

#     if direction == 'north':
        
#         encounter = random.randint(1,15)
#         if distance >= encounter:
#             distance = encounter
#             steps_n += distance
#             print(f"You only moved {distance} before encoutering a monster to fight!")
#             Easy_Combat_Sequence.easy_combat(health,player_character)
#             continue

#         else:
#             steps_n += distance
#             continue

#     if direction == 'south':
#         steps_s = steps_s + distance
#         return steps_s
    
#     if direction == 'east':
#         steps_e = steps_e + distance
#         return steps_e
    
#     if direction == 'west':
#         steps_w = steps_w + distance
#         return steps_w


