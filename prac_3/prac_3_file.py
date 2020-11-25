FILENAME = 'test.txt'


def create_file(filename):  # записываем строки в файл
    with open(filename, 'a', encoding='utf-8') as f:
        while True:
            input_str = input('введите строку:')
            f.write(input_str)
            f.write('\n')
            f.flush()  # моментальная запись на диск, без кэша


def read_text_file(filename):  # печатаем файл в консоль
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')


def read_bin_file(filename):  # читаем файл в бинарном режиме
    with open(filename, 'rb') as f_bin:
        print(f_bin.read())


def text_to_bin(filename):  # читаем файл в текстовом режиме и записываем его в бинарном
    with open(filename, 'rb') as f_bin_2:
        with open('output_' + filename, 'wb') as f_dst:
            for line in f_bin_2:
                f_dst.write(line)
                f_dst.flush()


if __name__ == '__main__':
    text_to_bin(FILENAME)
