k = 'ноутбук'
# Создаем словари для английского и русского алфавитов
english_scores = {"AEIOULNSTR": 1, "DG": 2, "BCMP": 3, "FHVWY": 4, "K": 5, "JX": 8, "QZ": 10}
russian_scores = {"АВЕИНОРСТ": 1, "ДКЛМПУ": 2, "БГЁЬЯ": 3, "ЙЫ": 4, "ЖЗХЦЧ": 5, "ШЭЮ": 8, "ФЩЪ": 10}

# Функция для подсчета стоимости слова
def word_score(word, scores):
    score = 0
    for letter in word.upper():
        for key, value in scores.items():
            if letter in key:
                score += value
    return score

# Получаем слово от пользователя
word = input('Введите слово: ')

# Определяем, на каком языке написано слово
if any(letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' for letter in word.upper()):
    scores = english_scores
else:
    scores = russian_scores

# Выводим стоимость слова
print("Стоимость слова", word, ":", word_score(word, scores))
