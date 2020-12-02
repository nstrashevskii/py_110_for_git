import re

emails = ['abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz']
IP4_PATTERN = re.compile(r'((25[0-5]|2[0-4]\d|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}'
                         r'(25[0-5]|2[0-4]\d|1[0-9][0-9]|[1-9][0-9]|[0-9])')


def task_1():
    first_word = re.compile(r'\b\w+\b')
    word_list = [
        ',./ sdfsdf',
        'Ddfsdf',
        '@@##,sdfsdf',
        '123_sdfsdf',
        '123sdfsdf',
        ', s,dfsdf',
        '123, fewfew',
    ]
    for word in word_list:
        print(first_word.search(word))


def test_correct_ip():
    ip_list = ['8.8.8.8', '192.168.1.1', '123.231.132.231', '12.123.12.12']
    for ip in ip_list:
        obj_match = IP4_PATTERN.fullmatch(ip)
        if obj_match is not None:
            print(obj_match.group())
        else:
            print(f'Не распознанный ip адрес {ip}')


def test_incorrect_ip():
    ip_list = [
        '3248.8.8.8',
        '192.43168.0.1',
        '345.0.0.1',
        '100.743.207.4',
        '100.143.207'
    ]

    for ip in ip_list:
        obj_match = IP4_PATTERN.fullmatch(ip)
        if obj_match is not None:
            print(obj_match.group())
        else:
            print(f'Не распознанный ip адрес {ip}')


def main():
    # test_correct_ip()
    # test_incorrect_ip()
    task_1()


if __name__ == '__main__':
    main()
