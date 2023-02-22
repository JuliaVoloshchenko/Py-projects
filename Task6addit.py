num = input('Введите шестизначное число: ')
a = int(num[0]) + int(num[1]) + int(num[2])
b = int(num[3]) + int(num[4]) + int(num[5])
if a == b:
    print('Yes')
else:
    print('No')