import os


def group_rename_files(directory, new_name, num_digits, old_ext, new_ext, name_range):
    # Получаем список файлов в указанном каталоге
    files = [f for f in os.listdir(directory) if f.endswith(old_ext)]

    # Сортируем файлы для последовательного переименования
    files.sort()

    # Переименовываем файлы
    for i, filename in enumerate(files):
        # Извлекаем часть оригинального имени файла по указанному диапазону
        original_part = filename[name_range[0] - 1:name_range[1]]

        # Формируем новый порядковый номер с ведущими нулями
        counter = str(i + 1).zfill(num_digits)

        # Формируем новое имя файла
        new_filename = f"{original_part}{new_name}{counter}.{new_ext}"

        # Полные пути к старому и новому файлу
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)

        # Переименовываем файл
        os.rename(old_file, new_file)
        print(f"Переименован: {old_file} -> {new_file}")


# Пример использования функции
directory = "путь_к_вашему_каталогу"
new_name = "новое_имя"
num_digits = 3
old_ext = "txt"
new_ext = "md"
name_range = (3, 6)

group_rename_files(directory, new_name, num_digits, old_ext, new_ext, name_range)