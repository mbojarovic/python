# Задача 1. Напишите программу, которая принимает на вход число N
# и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def fact(n):
    array = []
    res = 1
    for el in range(1, n + 1):
        res = res * el
        array.append(res)
    print(f"N = {n} -> {array}", end=" ")


# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
def func2():
    print(f"x y z ¬(X ∧ Y) ∨ Z")
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                print(f"{x} {y} {z}  {int((not x and y) or z)}")


# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

def func(first, second):
    for i in first:
        if i in second:
            res = second.count(i)
            print(f"{i} - {res}", end=" ")

# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

def func3(value: int):
    listArray = []
    for elements in range(-value, value+1):
        listArray.append(elements)
    listArray = listArray[-2:]
    for el in range(-value, value-1):
        listArray.append(el)

    print(f"{value} -> {listArray}")


