import datetime as date


def counter(fn):
    def wrapper(*args, **kwargs):
        # до вызова функции
        result = fn(*args, **kwargs)
        wrapper.count += 1
        print(f'Функция {fn.__name__} была вызвана {wrapper.count} раз')
        # после вызова функции
        return result

    wrapper.count = 0  # будет выполнено один раз на момент декорирования(инициализарование)
    return wrapper


def counter_main():
    @counter  # pow = counter(pow)
    def my_print():
        print(2)

    for _ in range(10):
        my_print()


def timeit(count=1):
    def time_func(fn):
        def wrapper(*args, **kwargs):
            total_time = 0
            for _ in range(count):
                t0 = date.datetime.now()
                fn(*args, **kwargs)
                t1 = date.datetime.now() - t0
                total_time += t1
            print(f'функция {fn.__name__} выполнялась {total_time / count}')

        return wrapper
    return time_func


def timeit_main():
    @timeit(10)
    def pow_():
        return 2 ** 20


def cache(fn):
    def wrapper(*args):
        local_cach = fn.__dict__  # кэш свой для каждой функции
        if args not in local_cach:
            result = fn(*args)
            local_cach[args] = result
        return local_cach[args]
    return wrapper


def cache_main():
    @cache
    def mul_2(n):
        return n * 2

    for i in range(10):
        print(mul_2(i))
        print(mul_2(i))


if __name__ == '__main__':
    #  time_main()
    # counter_main()
    # cache_main()
    timeit_main()