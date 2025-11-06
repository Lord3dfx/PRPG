class Inventory:

    __items = []

    def __init__(self):
        print('Inventory is created')

    def get_all_items(self):
        if not self.__items:
            return None
        names = []
        for item in self.__items:
            names.append(item['name'])
        return names

    def get_item(self, index):
        try:
            return self.__items[index-1]
        except IndexError:
            return None
        except ValueError:
            return None

    def add_item(self, item):
        self.__items.append(item)

    def remove_item(self, index):
        if index > len(self.__items):
            return None
        del self.__items[index-1]
        return True