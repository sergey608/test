def is_triangle(a, b, c):
    if a + b > c and a + c > b and c + b > a:
        return True
    else:
        return False

def triangle_type(a, b, c):
    if a == b == c:
        return "Равностороний"
    elif a == b or b == c or a == c:
        return "Равнобедренний"
    else:
        return "Разносторонний"

a = float(input("Введите переменную а: "))
b = float(input("Введите переменную b: "))
c = float(input("Введите переменную c: "))

if is_triangle(a, b, c):
    print("Треугольник существует")
    print("Тип треугольника", triangle_type(a, b, c))
else:
    print("Треугольник не существует")