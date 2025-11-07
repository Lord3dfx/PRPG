from inventory import Inventory
class Player:

    def __init__(self, name, race):
        self.__name = name
        self.__race = race
        self.__lvl = 1
        self.__exp = 0
        self.__inventory = Inventory()
        self.__update()
        self.__hp = self.__max_hp

    def __update(self):
        self.__attack_str = 2 * self.__lvl
        self.__max_hp = 5 * self.__lvl

    def level_up(self):
        self.__lvl += 1
        self.__exp = 0
        self.__update()
        self.__hp = self.__max_hp

    @property
    def hp(self):
        return self.__hp

    def take_damage(self, value):
        self.__hp -= value

    def healing(self, value):
        self.__hp += value

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def lvl(self):
        return self.__lvl

    @property
    def attack(self):
        return self.__attack_str

    @property
    def race(self):
        return self.__race
    @race.setter
    def race(self, value):
        self.__race = value

    @property
    def exp(self):
        return self.__exp

    def add_exp(self, value):
        self.__exp += value

    @property
    def max_hp(self):
        return self.__max_hp

    def add_item(self, item):
        self.__inventory.add_item(item)

    def get_all_items(self):
        return self.__inventory.get_all_items()

    def get_item(self, index):
        return self.__inventory.get_item(index)

    def get_info(self):
        print(f"""\033[97;1m Name: {self.__name} \033[0m, \033[97;43;1m LVL: {self.__lvl} \033[0m, \033[97;44;1m Race: {self.__race} \033[0m, \033[97;41;1m Attack: {self.__attack_str} \033[0m. \033[97;42;1m Current hp: {self.__hp} \033[0m,\033[97;45;1m EXP: {self.__exp} \033[0m (need \033[97;35;1m{(self.__lvl * 5) - self.__exp} \033[0mEXP to level up)
\033[3mReady for adventures...\033[0m\n""")