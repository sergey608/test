n = 111
ones = n % 10
tens = (n // 10) % 10
hundreds = n // 100
res = ones + tens + hundreds
print("Сумма цифр:", res)
