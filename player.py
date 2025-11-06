from inventory import Inventory
class Player:

    __name = ''
    __lvl = 1
    __race = ''
    __attack_str = 2 * __lvl
    __exp = 0
    __max_hp = 5 * __lvl
    __hp = 5 * __lvl
    __inventory = Inventory()


    def __init__(self, name, race):
        self.name = name
        self.race = race

    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, value):
        self.__hp = value

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
    @lvl.setter
    def lvl(self, value):
        self.__lvl += value

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
    @exp.setter
    def exp(self, value):
        self.__exp = value

    def add_exp(self, value):
        self.__exp += value

    @property
    def max_hp(self):
        return self.__max_hp
    @max_hp.setter
    def max_hp(self, value):
        self.__max_hp = value

    def add_item(self, item):
        self.__inventory.add_item(item)

    def get_all_items(self):
        return self.__inventory.get_all_items()

    def get_item(self, index):
        return self.__inventory.get_item(index)

    def get_info(self):
        print(f"""\033[97;47;1mName: {self.__name}\033[0m, \033[97;43;1mlvl: {self.__lvl}\033[0m, \033[97;44;1mrace: {self.__race}\033[0m, \033[97;41;1mattack: {self.__attack_str}\033[0m. \033[97;42;1mCurrent hp: {self.__hp}\033[0m
\033[3mReady for adventures...\033[0m\n""")