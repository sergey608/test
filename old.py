count = 0  # счетчик для подсчета количества возможных комбинаций
for быки in range(101):  # Максимальное количество быков, которое можно купить
    for коровы in range(101 - быки):  # Максимальное количество коров, которое можно купить после покупки быков
        телята = 100 - быки - коровы  # Оставшееся количество голов скота - это телята
        if быки * 10 + коровы * 5 + телята * 0.5 == 100:  # Если общая стоимость равна 100 рублей
            print(f"Комбинация {count + 1}: Быков: {быки}, Коров: {коровы}, Телят: {телята}")
            count += 1  # увеличиваем счетчик
print(f"Всего найдено {count} возможных комбинаций.")