# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

numbers = []
meanings = int(input('Укажите, сколько значений хотите записать в массив: '))
for i in range(1, meanings + 1):
    numbers.append((input(f'Введите значение {i}: ')))


def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


if checkPredicate(numbers) == True:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")