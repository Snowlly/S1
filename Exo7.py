numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
pair = 0
impair = 0

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        pair += 1
    else: 
        impair += 1

print("Nombre de pairs : ", pair)
print("Nombre d'impairs : ", impair)