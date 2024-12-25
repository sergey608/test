from datetime import datetime, timedelta


def get_future_date(days):
    # Получаем текущую дату и время
    now = datetime.now()

    # Создаем объект timedelta с указанным количеством дней
    future_date = now + timedelta(days=days)

    # Форматируем дату в строку в формате YYYY-MM-DD
    formatted_date = future_date.strftime('%Y-%m-%d')

    return formatted_date


# Пример использования
days = 10
future_date = get_future_date(days)
print(f"Дата через {days} дней: {future_date}")
