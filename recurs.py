def funct(n):
    a = input()
    if n == 1:
        return a
    return funct(n-1)+a

n = int(input())
print(funct(n))