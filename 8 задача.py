dlina_n = int(input('Введите количество долек по вертикали: \n'))
shirina_m = int(input('Введите количество долек по горизонтали: \n'))
otlomit_k = int(input('Введите, сколько нужно отломить долек: \n'))

while otlomit_k >= dlina_n * shirina_m:
    otlomit_k = int(input('Введите нормальное количество долек: \n'))

if dlina_n == otlomit_k or shirina_m == otlomit_k or otlomit_k % dlina_n == 0 or otlomit_k % shirina_m == 0:
    print('yes')
else:
    print('no')