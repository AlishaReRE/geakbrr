chislo = int(input("Введите общее число журавликов \n"))

while chislo % 2 != 0:
    chislo = int(input("Введите число корректно \n"))

Petya = Serezha = chislo // 6
Katya = 2 * (Petya + Serezha)

print("Катя: ", Katya, 'Сережа: ', Serezha, "Петя: ", Petya)