# Задача 1. Напишите программу, которая принимает на вход число N
# и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def fact(n):
    array = []
    res = 1
    for el in range(1, n+1):
        res = res * el
        array.append(res)
    print(f"N = {n} -> {array}", end=" ")
