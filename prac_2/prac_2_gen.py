def gen_1(str_):
    for word in str_.split():
        yield word


def count(start, step):
    current_value = start
    while True:
        new_start = yield current_value
        if new_start is None:
            current_value += step
        else:
            current_value = new_start

# домашнее задание
# в teams вторая часть занятия
# Написать генератор псевдо случайных чисел
# Генератор внутри задается какой-нибудь формулой, которая выдает «случайный» результ
# На вход генератору приходит seed – начальное значение,
# при одинаковых начальных значениях два генератора будут выдавать одинаковые следующие значения


if __name__ == '__main__':

    count_iter = count(5, 5)
    for _ in range(10):
        print(next(count_iter))

    count_iter.send(100)

    for _ in range(10):
        print(next(count_iter))
