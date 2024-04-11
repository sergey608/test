def copy_line(from_file, to_file, line_number):
    with open(from_file, 'r') as f1, open(to_file, 'a') as f2:
        lines = f1.readlines()
        if line_number > len(lines):
            return "Номер строки превышает количество строк в файле."
        else:
            f2.write(lines[line_number - 1])

# Пример использования функции
copy_line('file1.txt', 'file2.txt', 3)
