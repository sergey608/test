class Animal:
    def __init__(self, name, species, birth_date):
        self.name = name
        self.species = species
        self.birth_date = birth_date
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def get_commands(self):
        return self.commands

    def __str__(self):
        return f"{self.name} ({self.species}), родился {self.birth_date}"

class PetRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в реестр.")

    def view_animals(self):
        if not self.animals:
            print("Реестр пуст.")
        else:
            for animal in self.animals:
                print(animal)

    def update_animal(self, name, new_name=None, new_species=None, new_birth_date=None):
        for animal in self.animals:
            if animal.name == name:
                if new_name:
                    animal.name = new_name
                if new_species:
                    animal.species = new_species
                if new_birth_date:
                    animal.birth_date = new_birth_date
                print(f"Информация о животном {name} обновлена.")
                return
        print(f"Животное с именем {name} не найдено.")

    def delete_animal(self, name):
        for animal in self.animals:
            if animal.name == name:
                self.animals.remove(animal)
                print(f"Животное {name} удалено из реестра.")
                return
        print(f"Животное с именем {name} не найдено.")

    def train_animal(self, name, command):
        for animal in self.animals:
            if animal.name == name:
                animal.add_command(command)
                print(f"Животное {name} обучено команде '{command}'.")
                return
        print(f"Животное с именем {name} не найдено.")

class Counter:
    def __init__(self):
        self.count = 0
        self.closed = False

    def add(self):
        if self.closed:
            raise Exception("Ресурс закрыт")
        self.count += 1

    def close(self):
        self.closed = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

def main_menu():
    registry = PetRegistry()
    while True:
        print("\nМеню:")
        print("1. Завести новое животное")
        print("2. Просмотреть всех животных")
        print("3. Обновить информацию о животном")
        print("4. Удалить животное")
        print("5. Обучить животное новой команде")
        print("6. Выйти")
        choice = input("Выберите опцию: ")

        if choice == '1':
            name = input("Введите имя животного: ")
            species = input("Введите вид животного: ")
            birth_date = input("Введите дату рождения животного (YYYY-MM-DD): ")
            with Counter() as counter:
                if name and species and birth_date:
                    animal = Animal(name, species, birth_date)
                    registry.add_animal(animal)
                    counter.add()
                else:
                    print("Все поля должны быть заполнены.")
        elif choice == '2':
            registry.view_animals()
        elif choice == '3':
            name = input("Введите имя животного для обновления: ")
            new_name = input("Введите новое имя (оставьте пустым, если не нужно менять): ")
            new_species = input("Введите новый вид (оставьте пустым, если не нужно менять): ")
            new_birth_date = input("Введите новую дату рождения (оставьте пустым, если не нужно менять): ")
            registry.update_animal(name, new_name, new_species, new_birth_date)
        elif choice == '4':
            name = input("Введите имя животного для удаления: ")
            registry.delete_animal(name)
        elif choice == '5':
            name = input("Введите имя животного для обучения: ")
            command = input("Введите команду: ")
            registry.train_animal(name, command)
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main_menu()

#Объяснение кода:
#Класс Animal: Представляет животное с именем, видом, датой рождения и списком команд.
#Класс PetRegistry: Управляет реестром животных, включая добавление, просмотр, обновление, удаление и обучение животных.
#Класс Counter: Счетчик с методом add(), который увеличивает значение на 1 при добавлении нового животного. Реализует интерфейс контекстного менеджера для работы в блоке try-with-resources.
#Функция main_menu(): Реализует навигацию по меню для взаимодействия с пользователем.
#Этот код позволяет вам управлять реестром домашних животных, добавлять новые животные, обновлять их информацию, удалять и обучать новым командам