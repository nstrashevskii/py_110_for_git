FILENAME = 'test.txt'


def create_file(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        while True:
            input_str = input('введите строку')
            f.write(input_str)
            f.write('\n')





if __name__ == '__main__':

    create_file(FILENAME)