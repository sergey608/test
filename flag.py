import argparse


def main():
    # Создаем парсер аргументов
    parser = argparse.ArgumentParser(description="Скрипт для работы с аргументами командной строки")

    # Добавляем обязательные аргументы
    parser.add_argument("number", type=int, help="Число")
    parser.add_argument("text", type=str, help="Строка")

    # Добавляем опции
    parser.add_argument("--verbose", action="store_true", help="Вывод дополнительной информации")
    parser.add_argument("--repeat", type=int, help="Количество повторений строки")

    # Парсим аргументы
    args = parser.parse_args()

    # Выводим дополнительную информацию, если установлен флаг --verbose
    if args.verbose:
        print(f"Получено число: {args.number}")
        print(f"Получена строка: {args.text}")

    # Повторяем строку указанное количество раз, если установлен параметр --repeat
    if args.repeat:
        for _ in range(args.repeat):
            print(args.text)
    else:
        print(args.text)


if __name__ == "__main__":
    main()
