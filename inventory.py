class Inventory:

    def __init__(self):
        self.__items = []
        print('Inventory is created')

    def get_all_items(self):
        if not self.__items:
            return None
        result = []
        for i, item in enumerate(self.__items, 1):
            if item.get('quantity', 1) > 1:
                result.append(f"{i}. {item['name']} (x{item['quantity']})")
            else:
                result.append(f"{i}. {item['name']}")

        return "\n".join(result)

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