class PhoneBook:
    def __init__(self, filename):
        self.filename = filename
        self.entries = self.load_entries()

    def load_entries(self):
        entries = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    surname, name, patronymic, phone_number = line.strip().split(',')
                    entries.append({
                        'surname': surname,
                        'name': name,
                        'patronymic': patronymic,
                        'phone_number': phone_number
                    })
        except FileNotFoundError:
            pass
        return entries

    def save_entries(self):
        with open(self.filename, 'w' ) as file:
            for entry in self.entries:
                file.write(','.join(entry.values()) + '\n')

    def add_entry(self, surname, name, patronymic, phone_number):
        # Проверяем, есть ли уже такая запись в справочнике
        if not any(e['surname'] == surname and e['name'] == name and e['patronymic'] == patronymic and e['phone_number'] == phone_number for e in self.entries):
            self.entries.append({
                'surname': surname,
                'name': name,
                'patronymic': patronymic,
                'phone_number': phone_number
            })
            self.save_entries()

    def search_entries(self, search_value):
        return [entry for entry in self.entries if search_value in entry['name'] or search_value in entry['surname']]

    def copy_entry(self, from_file, to_file, line_number):
        with open(from_file, 'r') as f1, open(to_file, 'a') as f2:
            lines = f1.readlines()
            if line_number > len(lines):
                return "Номер строки превышает количество строк в файле."
            else:
                f2.write(lines[line_number - 1])

# Пример использования
phonebook = PhoneBook('phonebook.txt')  # Создаем новый телефонный справочник
phonebook.add_entry('Иванов', 'Иван', 'Иванович', '+79001234567')  # Добавляем запись
phonebook.add_entry('Кузьмин', 'Кирилл', 'Михалыч', '+7900127865')  # Добавляем запись

# Выводим все записи в справочнике
for entry in phonebook.entries:
    print(entry)

def same_by(characteristic, objects):
    if not objects:
        return True
    characteristics = [characteristic(obj) for obj in objects]
    return len(set(characteristics)) == 1

objects = [2, 4, 6, 8]
print(same_by(lambda x: x % 2, objects))  # Выводим результат функции same_by
