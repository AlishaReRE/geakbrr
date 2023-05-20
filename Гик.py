chislo = int(input("Введите трехзначное число \n"))

while chislo >= 1000 or chislo < 100:
    chislo = int(input("Введите трехзначное число корректно \n"))

chislo_1 = chislo % 10
chislo_2 = chislo // 100
chislo_3 = (chislo // 10) % 10

print("Сумма равна:", chislo_1 + chislo_2 + chislo_3)