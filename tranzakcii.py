def format_seconds(seconds):
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{days} days {hours} hours {minutes} minutes {seconds} seconds"

# Пример использования:
print(format_seconds(123456))  # Вывод: '1 days 10 hours 17 minutes 36 seconds'


for number in range(1, 11):
    if number % 2 == 0:
        print(number, end=", ")
# Вывод: 2, 4, 6, 8, 10