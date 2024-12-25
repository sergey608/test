
#Задание на картинке требует отсортировать список чисел без использования встроенных методов
#сортировки. Один из способов сделать это - использовать сортировку пузырьком.
#Вот пример кода на Python

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Пример использования
input_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(input_list)
print(f"Отсортированный список: {sorted_list}")