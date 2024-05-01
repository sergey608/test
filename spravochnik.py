contact_data = {
    'first_name': None,
    'second_name': None,
    'phone_number': None,
}

def ask_data():
    s_name = input("Введите фамилию: ")
    f_name = input("Введите имя: ")
    m_name = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")
    contact = {'second_name': s_name,
               'first_name': f_name,
               'middle_name': m_name,
               'phone_number': phone}
    return contact

def add_new_contact():
    contact = ask_data()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(';'.join(contact.values()))
        file.write('\n')
    return True

def open_phonebook():
    title = ["Фамилия", "Имя", "Отчество", "Телефон"]
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        print("\t\t".join(title))
        for line in file:
            print("\t\t".join(line.strip().split(";")))

def find_contact():
    print(f"Поиск по:\n1 имени\n2 фамилии\n3 отчеству\n4 номеру\n0 выход")
    choice = int(input("Выберите опцию: "))
    search_term = input("Введите искомое значение: ")
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        for line in file:
            contact = line.strip().split(";")
            if (choice == 1 and contact[1] == search_term) or \
                    (choice == 2 and contact[0] == search_term) or \
                    (choice == 3 and contact[2] == search_term) or \
                    (choice == 4 and contact[3] == search_term):
                print("\t\t".join(contact))

def copy_contact():
    source_file = 'phonebook.txt'
    target_file = input("Введите имя целевого файла: ") + '.txt'
    open_phonebook()
    line_number = int(input("Введите номер строки, которую нужно скопировать: "))

    with open(source_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if line_number > len(lines) or line_number < 0:
        print("Нет строки с таким номером.")
        return

    with open(target_file, 'a', encoding='utf-8') as file:
        file.write(lines[line_number - 1])

    print("Контакт успешно скопирован.")