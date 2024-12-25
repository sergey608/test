import random
import datetime

# Определяем пользовательские исключения
class KillError(Exception):
    pass

class DrunkError(Exception):
    pass

class CarCrashError(Exception):
    pass

class GluttonyError(Exception):
    pass

class DepressionError(Exception):
    pass

# Функция, которая возвращает количество кармы и может выкинуть исключение
def one_day():
    karma = random.randint(1, 7)
    if random.randint(1, 10) == 1:
        raise random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])()
    return karma

# Основная программа
def main():
    total_karma = 0
    goal_karma = 500

    with open("karma.log", "a") as log_file:
        while total_karma < goal_karma:
            try:
                total_karma += one_day()
            except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as e:
                log_file.write(f"{datetime.datetime.now()}: {e.__class__.__name__}\n")
            print(f"Current karma: {total_karma}")

if __name__ == "__main__":
    main()
import random
import datetime

# Определяем пользовательские исключения
class KillError(Exception):
    pass

class DrunkError(Exception):
    pass

class CarCrashError(Exception):
    pass

class GluttonyError(Exception):
    pass

class DepressionError(Exception):
    pass

# Функция, которая возвращает количество кармы и может выкинуть исключение
def one_day():
    karma = random.randint(1, 7)
    if random.randint(1, 10) == 1:
        raise random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])()
    return karma

# Основная программа
def main():
    total_karma = 0
    goal_karma = 500

    with open("karma.log", "a") as log_file:
        while total_karma < goal_karma:
            try:
                total_karma += one_day()
            except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as e:
                log_file.write(f"{datetime.datetime.now()}: {e.__class__.__name__}\n")
            print(f"Current karma: {total_karma}")

if __name__ == "__main__":
    main()
