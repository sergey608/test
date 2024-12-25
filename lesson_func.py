# Задание на картинке требует написать функцию, которая принимает на вход три списка одинаковой длины:
# имена (str), ставки (int) и премии (str) в виде процентов.
# Функция должна вернуть словарь, где ключами будут имена, а значениями
# - сумма премии, рассчитанная как ставка, умноженная на процент премии.


def calculate_bonus(names, rates, bonuses):
    result = {}
    for name, rate, bonus in zip(names, rates, bonuses):
        percentage = float(bonus.strip('%')) / 100
        result[name] = rate * percentage
    return result

# Пример использования
names = ["Alice", "Bob", "Charlie"]
rates = [1000, 1500, 2000]
bonuses = ["10.25%", "15.50%", "20.00%"]

bonus_dict = calculate_bonus(names, rates, bonuses)
print(bonus_dict)