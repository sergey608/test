class Animal:
    def __init__(self, name, birth_date):
        self.__name = name
        self.__birth_date = birth_date

    def get_name(self):
        return self.__name

    def get_birth_date(self):
        return self.__birth_date

class Equine(Animal):
    def __init__(self, name, birth_date, type):
        super().__init__(name, birth_date)
        self.__type = type

    def get_type(self):
        return self.__type

# Пример использования
horse = Equine("Buddy", "2018-05-10", "Horse")
print(horse.get_name())  # Вывод: Buddy
print(horse.get_type())  # Вывод: Horse