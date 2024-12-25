def draw_frame(width, height):
    print('-' * width)


    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')

    print('-' * width)

width = int(input("Введите ширину рамки: "))
height = int(input("Введите высоту рамки: "))

draw_frame(width, height)