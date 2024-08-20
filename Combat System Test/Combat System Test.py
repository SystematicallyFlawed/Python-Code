##An attempt at making a combat system##

import sys
import random

input1 = int(input("Input a number "))
input2 = int(input("Input a number "))
input3 = int(input("Input a number "))
input4 = int(input("Input a number "))
input5 = int(input("Input a number "))
input_list = [input1, input2, input3, input4, input5]

enemy_health = input_list.pop()
enemy_damage = input_list.pop()
player_health = input_list.pop()
player_damage = input_list.pop()
player_damage_defended = input_list.pop()
enemy_choices = ["attack", "defend", "idle"]

print(f"The enemy has {enemy_health} health")
print(f"The enemy deals {enemy_damage} damage")
print(f"You have {player_health} health")
print(f"You deal {player_damage} damage")
print(f"You deal {player_damage_defended} damage when also attacked")

def combat():
    player_action = input("Do you attack or defend? ").lower()
    global player_health, enemy_health
    enemy_action = random.choice(enemy_choices)
 
    if enemy_action == "attack":
        if player_action == "attack":
            player_health -= enemy_damage
            enemy_health -= player_damage_defended
            print(f"You take {enemy_damage} damage")
            print(f"The enemy takes {player_damage_defended} damage")
        else:
            print("You take no damage")
    elif enemy_action == "defend":
        if player_action == "attack":
            print("The enemy defends, and takes no damage")
        else:
            print("No one takes any damage")
    elif enemy_action == "idle":
        if player_action == "attack":
            enemy_health -= player_damage
            print(f"You hit the enemy for {player_damage} damage")
        else:
            print("No one takes any damage")  

while enemy_health > 0 and player_health > 0:
    combat()
    
if player_health <= 0:
    print("You have died like a loser")
elif enemy_health <= 0:
    print("You have brutally slaughtered your enemy")

input("Press enter to exit")
sys.exit()