letter = input()
alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
if letter == alphabet[-1]:
    print("Дальше буквы нет")
else:
    next_letter_index = alphabet.index(letter) + 1
    next_letter = alphabet[next_letter_index]
    print(next_letter)
