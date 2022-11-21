# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.

from math import sqrt

xa, ya = int(input('Введите координату Х для точки А: ')), int(input('Введите координату Y для точки A: '))
xb, yb = int(input('Введите координату Х для точки B: ')), int(input('Введите координату Y для точки B: '))
result = sqrt((xa - xb)**2 + (ya - yb)**2)
print(f'Расстояние между точками: {result}')