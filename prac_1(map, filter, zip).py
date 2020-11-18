import itertools as it
import random

# start = 100
# step = 7
# for i in itertools.count(start, step):
#     print(i)

# users = ['lol', 'kek', 'chebureck']
# counter = ['loli', 'pop' ]
#
# iter_users = itertools.cycle(users)
# current_user = users[0]
#
# for _ in counter:
#     iter_users
#
# print(current_user)
from math import sqrt
import operator as op


# def _get_dist(point):
#     return sqrt(point[0] ** 2 + point[1] ** 2)


def map_1():
    """
    Дан список точек, найти самую удаленную точку от начала координат
    :return:
    """
    pts = [
        (3, 4),
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]

    # list_dist = list(map(_get_dist, pts))
    # print(list_dist)
    # print(max(list_dist))
    print(max(map(lambda point: sqrt(point[0] ** 2 + point[1] ** 2), pts)))


def map_2():
    """
    Дан список чисел в различных форматах, привести их к типу int
    :return:
    """
    num_list = [
        "12",
        "14",
        3.1415926,
        5,
        0xFF,
        0b1010101010
    ]

    print(list(map(int, num_list)))


def _round(a, n=2):
    return round(a, n)


def map_3():
    """
    Дан список чисел округлить их до 2 знаков после запятой
    :return:
    """
    my_floats = [
        4.356345,
        6.0934,
        3.245235,
        9.77545,
        2.164234234,
        8.884234235,
        4.595235346645
    ]
    # print(list(map(_round, my_floats)))
    print(list(map(round, my_floats, [2] * len(my_floats))))


def map_4():
    """
    Найти длину самого длинного слова
    :return:
    """
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]
    print(max(map(len, list_words)))


def map_5():
    """
    Перевести все слова в верхний регистр
    :return:
    """
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]
    print(list(map(str.upper, list_words)))


# def _summa(l_1, l_2):
#     return l_1 + l_2


def map_6():
    """
    Поэлементно сложить два списка
    :return:
    """
    list_1 = [5, 2, 3]
    list_2 = [5, 2, 4]
    print(list(map(op.add, list_1, list_2)))


def map_7():
    a = [
        [2, 3, 5, 7],
        [11, 13, 17, 19],
        [23, 29],
        [31, 37]
    ]
    print(list(map(len, a)))  # Найти длину всех последовательностей
    print(sum(map(len, a)))  # Найти общее количество элементов в списке
    print(max(map(len, a)))  # Найти общее количество элементов в списке


# filter

def check_odd(n):
    return not n % 2


# def pow_2(n):
#     return n ** 2


def filter_1():
    N = 10
    all_number = it.count(1, 1)
    all_odd = filter(check_odd, all_number)
    all_odd_pow_2 = map(lambda n: n ** 2, all_odd)

    for _ in range(N):
        print(next(all_odd_pow_2))


def otr(n):
    return n < 0 and n % 3 == 0


def filter_2():
    """
    получить все отрицательные числа кратные трем
    :return:
    """
    n = 100
    list_num = [random.randint(-100, 100) for _ in range(n)]
    print(list(filter(otr, list_num)))


# def sravnen(_str='lkdfdlf lvdkfddl dddcd', list_1):
#     for i in range(len(list_1)):
#         for j in _str:
#             return i == j
#
#
# def filter_3():
#     """
#     Дана входная строка и массив чисел,
#     необходимо вернуть строку с теми буквами,
#     которые стоят на указанных местах (два варианта, используя и не используя list comprehensions)
#     :return:
#     """
#     _str = 'lkdfdlf lvdkfddl dddcd'
#     list_1 = [2, 1, 5, 10]
#     print(list(filter(sravnen, list_1)))

# def get_char(i, str_):
#     return op.getitem(str_, i)


def filter_3():
    """
    как сделать через filter и используя list comprehensions
    Дана входная строка и массив чисел,
    необходимо вернуть строку с теми буквами,
    которые стоят на указанных местах (два варианта, используя и не используя list comprehensions)
    :return:
    """
    i = [1, 3, 5, 6]
    print(list(map(lambda i, str_: op.getitem(str_, i), i, it.repeat('loollo loooll lloll', len(i)))))


def zip_1():
    fig = ['квадрат', 'ромб', 'круг', 'овал']
    colors = ['красный', 'синий', 'зеленый']
    def_color = 'желтый'
    print(list(zip(fig, colors)))
    print('-----')
    for figura, color in it.zip_longest(fig, colors, fillvalue=def_color):
        print(f"фигура {figura} окрашена в {color} цвет")
    print('-----')
    for figura, color in zip(fig, colors):
        print(f"фигура {figura} окрашена в {color} цвет")


def zip_2_enumerate(start, step):
    str_ = 'lolo ldlfdl'
    print(list(zip(range(start, len(str_), step), str_[start::step])))


# def index(a):
#     return
#
#
# def zip_3_map():
#     a = [1, 2, 3]
#     print(list(map(index, a)))

# debugger practice
def debug():
    print('1')
    print('2')
    print('3')
    print('4')


def loop_for():
    for i in range(-100, 100):
        print(i)


if __name__ == '__main__':
    loop_for()
