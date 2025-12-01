print("Saissez votre texte : ")
text = input()
l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
n = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letter = 0
number = 0

for i in range(len(l)):
    letter += text.count(str(l[i]))
for j in range(len(n)):
        number += text.count(str(n[j]))

print("Nombre de lettres : ", letter)
print("Nombre de chiffres : ", number)