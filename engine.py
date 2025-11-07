import items
from player import *
from dungeon import *
import time
import random

races = ('Human', 'Dwarf', 'Elf')

def debug_menu(player: Player):
    print('Entering debug mode...')
    while True:
        print(f'Loading player...')
        print("""DEBUG! Select an option:
        1. Generate dungeon
        2. DUNGEON TEST!!!
        q. Quit""")

        option = input('Select an option: ')
        match option:
            case '1':
                dungeon = Dungeon(player)
                print(dungeon.build_dungeon())
                del dungeon
            case '2':
                dungeon = Dungeon(player)
                dungeon.dungeon_menu()
                del dungeon
            case 'q':
                break

def inventory_menu(player: Player):
    print("Let's see, what in your bag...")
    while True:
        all_items = player.get_all_items()
        if not all_items:
            print("Your bag is empty...")
            break
        print("""Select an option:
    1. View all items
    2. Use item
    3. Close bag""")
        option = input('Select an option: ')
        match option:
            case '1':
                print(all_items)
            case '2':
                option = input('What item would you choose? \n')
                if option == '':
                    print('Something went wrong... Try again')
                    return
                player.use_item(int(option))
            case '3':
                break
            case _:
                print('Sorry, I don\'t understand that')
                continue


def delayed_print(text, delayed=0.5):
    print(text)
    time.sleep(delayed)

def moving_in_dungeon():
    delayed_print("""There is two ways, where you can go... What would you choose?
            1. Turn left
            2. Turn right
            3. Get your info
            4. Look at your inventory
            5. Exit the dungeon""")
    result = input('Your option: ')
    return result

def check_win_condition(monster: Monster, player: Player):
    if monster.hp <= 0:
        delayed_print(f"The \033[97;47;1m {monster.get_name()} \033[0m is defeated!", 1)
        delayed_print(f"You get an {monster.get_lvl() + monster.get_max_hp()} EXP!")
        player.add_exp(monster.get_lvl() + monster.get_max_hp())
        return True
    elif player.hp <= 0:
        delayed_print(f"Oh! The \033[97;47;1m {monster.get_name()} \033[0m is defeat you!", 1)
        delayed_print("Return into the village...")
        player.restore()
        return True
    else:
        return False



def create_player():
    while True:
        name = input("Enter your name: ")
        race = input("""Select your race:
        1. Human
        2. Dwarf
        3. Elf
        """)
        if race not in "123" or race == '':
            print("Failed to create character. Try again...\n")
            continue
        return Player(name, races[int(race)-1])

def dungeon_entering(player):
    delayed_print('Entering the dungeon...')
    while True:
        option = moving_in_dungeon()
        if option == '1':
            dice = random.randint(1, 10)
            if dice in range(1, 4):
                item = items.get_consumable_item(random.randint(1, 6))
                delayed_print(f'You found a treasure! This is {item['name']}!')
                if not player.add_item(item):
                    print(f'Oops! you dont have enough slots in bag. {item["name"]} has been dropped!')
            elif dice in range(4, 7):
                delayed_print('You see some skelets...')
            elif dice in range(7, 11):
                pass
             #  result = battle_start(player)
             #  if result:
             #      continue
             # else:
             #      break
        elif option == '2':
            dice = random.randint(1, 10)
            if dice in range(1, 4):
                delayed_print('Oh. Some cute shrooms...')
            elif dice in range(4, 7):
                delayed_print('Some sticky mud on the floor... Ewww...')
            elif dice in range(7, 11):
                battle_start(player)
        elif option == '3':
            print(player.get_info())
        elif option == '4':
            inventory_menu(player)
        elif option == '5':
            delayed_print('Returning to the village...')
            return
        else:
            print('Failed to enter the dungeon. Try again...\n')

def main_game(player):
    print(f"Welcome, {player.name}, your race is {player.race}. ")
    while True:
        print("""Select, what you would to do:
            1. Your stats
            2. Shop
            3. Your inventory
            4. Go to the dungeon...
            5. Return to main menu""")
        option = input("Enter your option: ")
        match option:
            case "1":
                player.get_info()
            case "2":
                print('Shop is closed right now...')
            case "3":
                inventory_menu(player)
            case "4":
                dungeon_entering(player)
            case "5":
                print("Returning to menu...")
                time.sleep(1)
                break
            case "6":
                debug_menu(player)
            case _:
                print("Invalid option, please try again.")
