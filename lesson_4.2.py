text = input("Введите текст: ")
words = text.split()
unique_words = set(words)
count_unique_words = len(unique_words)
print(count_unique_words)