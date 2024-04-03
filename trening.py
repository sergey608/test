num = int(input('Введите чило: '))
flag = True

for i in range(2, num):
    if num % i == 0:  #  если исходное число делится на какое-либо отличное от 1 и самого себя
        flag = False

if num == 1:
    print('Это единица, она не простая и не составная')
elif flag == True:
    print('Число простое')
else:
    print('Число составное')