lambda_func = lambda x: x + 1

# замыкание

def add(n):
    def inline_add(x):
        return x + n
    return inline_add


lambda_func = lambda n: lambda x: x + n

add_5 = lambda_func(5)

# Создать список, в котором каждый элемент – кортеж из двух чисел.
# Отсортировать данный список по убыванию вторых элементов кортежей.

n = 10
list_tuple = [(i, n+i) for i in range(n + 1)]
print(list_tuple)


def lambda_1():
    n = 10
    list_tuple = [(i, n + i) for i in range(n + 1)]
    l = sorted(list_tuple, key=lambda tuple_: tuple_[1], reverse=True)
    print(l)


def lambda_2():
    list_word = ['asad', 'ddf', 'lels', 'sdsdasd']
    l_1 = sorted(list_word, key=lambda word: len(word), reverse=True)
    print(l_1)


if __name__ == '__main__':
    lambda_2()