import random

firstname = ['Filthy', 'Deadly', 'Scary', 'Peachy', 'Blobbing', 'Slowly', 'Gigantic']
secondname = ['Goblin', 'Orc', 'Evileye', 'Wurm', 'Gnoll', 'Spider', 'Bat']

class Monster:

    def __init__(self, player):
        self.__name = firstname[random.randint(0, len(firstname)-1)] + ' ' + secondname[random.randint(0, len(secondname)-1)]
        self.__lvl = random.randint(player.lvl, player.lvl + 1)
        self.__atk = self.__lvl + 1
        self.__hp = self.__lvl * 3
        self.__max_hp = self.__lvl * 3

    def __del__(self):
        print('Object deleted...')

    def get_name(self):
        return self.__name

    def get_max_hp(self):
        return self.__max_hp

    def get_lvl(self):
        return self.__lvl

    def get_atk(self):
        return self.__atk

    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, value):
        self.__hp = value

    def get_info(self):
        print(f"""\033[97;1mName: {self.__name}\033[0m, \033[97;43;1mlvl: {self.__lvl}\033[0m, \033[97;41;1mattack: {self.__atk}\033[0m. \033[97;42;1mCurrent hp: {self.__hp}\033[0m""")