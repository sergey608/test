import math


def find_farthest_orbit(list_of_orbits):
    # Вычисляем площади всех орбит
    areas = [math.pi * a * b for (a, b) in list_of_orbits]

    # Находим максимальную площадь
    max_area = max(areas)

    # Ищем орбиту с максимальной площадью
    farthest_orbit = list_of_orbits[areas.index(max_area)]

    return farthest_orbit


# Список орбит
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# Вызываем функцию и выводим результат
print(find_farthest_orbit(orbits))
