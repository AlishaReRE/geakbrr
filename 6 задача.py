chislo = int(input("Введите номер билетика и узнайте, счастливый ли он \n"))

prav_1 = chislo % 10
prav_2 = (chislo % 100) // 10
prav_3 = (chislo % 1000) // 100

lev_1 = chislo // 100000
lev_2 = (chislo // 10000) % 10
lev_3 = (chislo // 1000) % 10

if (prav_1 + prav_2 + prav_3) == (lev_1 + lev_2 + lev_3):
    print("yes")
else:
    print("sorry, no")
