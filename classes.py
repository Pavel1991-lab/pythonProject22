from abc import abstractmethod
from typing import Dict

class Abstractstorage:
    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_item(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass

class BaseStorage(Abstractstorage):
    def __init__(self, items, capacity):
        self.__items = items
        self.capacity = capacity

    def add(self, name: str, amount: int):
        if self.get_free_space() < amount:
            print("Нет места")
            return
        if name.capitalize() not in self.__items:
            self.__items[name.lower()] = amount

        else:
            self.__items[name.capitalize()] += amount
        # if self.get_free_space() < amount:
        #     print("Нет места")

    def remove(self, name: str, amount: int):
        if name.capitalize() not in self.__items:
            print(f"Ошибка: продукт {name} отсутствует")
            return
        if self.__items[name.capitalize()]< amount:
            print(f"Ошибка: на складе недостаточно {name}")
            return

        self.__items[name.capitalize()] -= amount
        if self.__items[name.capitalize()] == 0:
            del self.__items[name]

    def get_free_space(self):
        return self.capacity - sum(self.__items.values())

    def get_item(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)


class Store(BaseStorage):
    def __init__(self, items: dict, capacity=100):
        super().__init__(items, capacity)


class Shop(BaseStorage):
    def __init__(self, items: dict, capacity=100):
        super().__init__(items, capacity)

    def add(self, name:str, amount:int):
       if name not in self.get_item() and self.get_unique_items_count() >= 5:
           print('Ошибка')
       super().add(name,amount)



class Requests:
    def __init__(self, request: str, storages: Dict[str, Abstractstorage]):
        parsed_request = request.lower().split(' ')
        if len(parsed_request) != 7:
            print('Ошибка')

        self.amount = int(parsed_request[1])
        self.product = parsed_request[2]
        self.depature = parsed_request[4]
        self.destination = parsed_request[6]

        if self.depature not in storages or self.destination not in storages:
            print ("Ошибка")
