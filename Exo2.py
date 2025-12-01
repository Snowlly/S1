import statistics

print("Entrez un premier nombre : ")
num1 = input()
print("Entrez un deuxieme nombre : ")
num2 = input()
print("Entrez un troisieme nombre : ")
num3 = input()

print("Médian : ", statistics.median([float(num1), float(num2), float(num3)]))