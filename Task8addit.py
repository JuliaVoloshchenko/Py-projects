n = int(input('Введите кол-во долек(ширина): '))
m = int(input('Введите кол-во долек(длина): '))
k = int(input('Введите сколько долек нужно отломить: '))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('Yes')
else:
    print('No')