# Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).

x = int(input('Введите номер четверти арабскими цифрами (в диапазоне от 1 до 4): '))

if x == 1:
    print('x > 0 , y > 0')
elif x == 2:
    print('x < 0, y > 0')
elif x == 3:
    print('x < 0, y < 0')
elif x == 4:
    print('x > 0, y < 0')
else:
    print('Вы ввели что-то другое')

