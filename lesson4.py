# Задача 1. Дано натуральное число N. Напишите метод,
# который вернёт список простых множителей числа N и количество этих множителей.
# 60 -> 2, 2, 3, 5
import math


def prime_factors(num):
    print(f"{num} ->", end=" ")
    while num % 2 == 0:
        print(2, end=" ")
        num = num / 2

    for i in range(3, int(math.sqrt(num)) + 1, 2):

        while num % i == 0:
            print(i, end=" ")
            num = num / i
    if num > 2:
        print(int(num), end=" ")