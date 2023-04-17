# Задача 1. Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8


def fib(n):
    fib1 = fib2 = 1
    arr = [fib1, fib2]

    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        arr.append(fib2)
        print(f"{n} -> {arr}")