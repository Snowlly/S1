a = 0
b = 1
c = b


while c < 50:
    print(c)
    res = a + b
    a, b = b, c
    c = a + b