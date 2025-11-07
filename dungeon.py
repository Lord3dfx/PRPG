from monsters import Monster
import textbase
import random
import items
import time
class Dungeon:

    def __init__(self, player):
        self.player = player
        self.monster = None
        self.events = []

    def delayed_print(self, text, delayed=0.5):
        print(text)
        time.sleep(delayed)

    def check_win_condition(self, monster, player):
        if monster.hp <= 0:
            self.delayed_print(f"The \033[97;47;1m {monster.get_name()} \033[0m is defeated!", 1)
            self.delayed_print(f"You get an {monster.get_lvl() + monster.get_max_hp()} EXP!")
            player.add_exp(monster.get_lvl() + monster.get_max_hp())
            return True
        elif player.hp <= 0:
            self.delayed_print(f"Oh! The \033[97;47;1m {monster.get_name()} \033[0m is defeat you!", 1)
            self.delayed_print("Return into the village...")
            player.restore()
            return True
        else:
            return False

    def battle_start(self,monster, player):
        turn = 'player'
        self.delayed_print('Watch out!!!', 1)
        self.delayed_print(f"This is\033[97;1m {monster.get_name()}\033[0m!!! He is a \033[97;43;1m {monster.get_lvl()} \033[0m LVL.")
        self.delayed_print(f"Now you must to fight!!!")
        while True:
            if turn == 'player':
                print(f"""It's your turn. What you want to do?
                1. Attack monster. Your attack is \033[97;41;1m {player.attack} \033[0m
                2. Show monster info
                3. Try to escape (You wil loose \033[97;41;1m {monster.get_atk()} \033[0m HP)""")
                option = input('Your option: ')
                match option:
                    case '1':
                        print('BAM!!!')
                        monster.hp = monster.hp - player.attack
                        self.delayed_print(f"You deal \033[97;41;1m {player.attack} \033[0mHP to the monster!")
                        if self.check_win_condition(monster, player):
                            break
                        turn = 'monster'
                    case '2':
                        monster.get_info()
                    case '3':
                        self.delayed_print('You are running with shame from the monster...', 1)
                        del monster
                        break
                    case _:
                        print('Sorry, I didn\'t understand that')
                        continue
            elif turn == 'monster':
                self.delayed_print(f"Now it's \033[97;47;1m {monster.get_name()}'s \033[0m turn!", 1)
                player.take_damage(monster.get_atk())
                if self.check_win_condition(monster, player):
                    return False
                self.delayed_print(
                    f"He's kicked you on \033[97;41;1m {monster.get_atk()} \033[0m HP!. Your HP is {player.hp}", 1)
                turn = 'player'
        return True

    def generate_chest(self):
        dice = random.randint(1, 4)
        match dice:
            case 1:
                self.events.append({'type':'chest', 'reward': True})
            case 2:
                self.events.append({'type':'chest', 'reward': False})
            case 3:
                self.events.append({'type':'chest_mimic', 'reward': True})
            case 4:
                self.events.append({'type':'chest_mimic', 'reward': False})

    def generate_trap(self):
        dice = random.randint(1, 3)
        self.events.append({'type':'trap', 'difficulty': dice})

    def generate_monster(self):
        self.events.append({'type':'monster'})

    def build_dungeon(self):
        for i in range(random.randint(1, 5)):
            dice = random.randint(1, 3)
            match dice:
                case 1:
                    self.generate_trap()
                case 2:
                    self.generate_chest()
                case 3:
                    self.generate_monster()

        return list(self.events)

    def react_to_choice(self, event):
        print(event)
        if event == 'chest':
            item = items.get_consumable_item(random.randint(1, 6))
            print(f'You get a {item['name']}')
            self.player.add_item(item)
            return True
        elif event == 'chest_mimic':
            item = items.get_consumable_item(random.randint(1, 6))
            self.player.add_item(item)
            self.player.take_damage(2)
            print(f"Oh, it was mimic! You got {item['name']} and 2 damage!")
            return True
        elif event == 'trap':
            print(f"You stuck in trap! You got 4 damage!")
            self.player.take_damage(4)
            return True
        elif event == 'monster':

            self.battle_start(self.monster, self.player)

        return False

    def clear_events(self):
        self.events = []

    def dungeon_menu(self):
        self.build_dungeon()
        option_number = 1
        print(f'{textbase.get_room_name()}')
        while True:
            for event in self.events:
                if event['type'] == 'chest':
                    print(f'{option_number}. {textbase.get_chest_name()}')
                elif event['type'] == 'trap':
                    print(f'{option_number}. {textbase.get_trap_name(event)}')
                elif event['type'] == 'monster':
                    self.monster = Monster(self.player)
                    print(f'{option_number}. Oh! {self.monster.get_name()} is here and he is {self.monster.get_lvl()} LVL!')
                option_number += 1
            option_number = 1
            print("'e' for leaving dungeon")
            option = input('Your choice: ')

            if option == 'e':
                break

            result = self.react_to_choice(self.events[int(option)-1]['type'])
            if result:
                self.events.pop(int(option)-1)
            else:
                self.delayed_print('Sorry, I didn\'t understand that')
                continue

        self.clear_events()


