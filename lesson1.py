# Задача 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и выводит название этого дня недели.
# 1 –> Понедельник
# 10 –> Нет такого дня
# 7 –> Воскресение

def week(number):
    if 7 >= number > 0:
        days_of_the_week = {
            'Monday': 1, 'Tuesday': 2, 'Wednesday': 3,
            'Thursday': 4, 'Friday': 5, 'Saturday': 6,
            'Sunday': 7}
        for day, num in dict.items(days_of_the_week):
            if number is num:
                print(day)
    else:
        print('дни недели от 1 до 7')


# Задача 2. Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09 !!!!!!! должно быть 5,1!!!!!!!!!
# A (7,-5); B (1,-1) -> 7,21

def shortestDistance(x1, y1, x2, y2):
    return print(round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2))


# Задача 3. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
# 1 -> x > 0, y > 0

def func(number):
    if type(number) != str:
        if 4 >= number > 0:
            if 1:
                print("Точка в I четверти x > 0 and y > 0")
            elif 2:
                print("Точка во II четверти x < 0 and y > 0")
            elif 3:
                print("Точка в III четверти x < 0 and y < 0")
            elif 4:
                print("Точка в IV четверти x > 0 and y < 0")
    else:
        print('всего 4 четверти оси координат')

