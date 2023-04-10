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


week()
