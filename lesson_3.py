# Входные данные
data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
        {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

# Создаем множество для хранения уникальных значений
unique_values = set()

# Проходим по каждому словарю в списке
for dictionary in data:
    # Проходим по каждому значению в словаре
    for value in dictionary.values():
        # Добавляем значение в множество
        unique_values.add(value.strip())

# Выводим уникальные значения
print(unique_values)

