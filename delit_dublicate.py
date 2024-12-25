def find_duplicates(input_list):
    duplicates = []
    for item in input_list:
        if input_list.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

# Пример использования
input_list = [1, 2, 3, 2, 4, 5, 3, 6, 4, 4]
result = find_duplicates(input_list)
print(f"Список дублирующихся элементов: {result}")