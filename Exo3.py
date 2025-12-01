a = 0
b = 1
c = b


while a < 50:
    print(a)
    res = a + b
    a, b = b, c
    c = a + b