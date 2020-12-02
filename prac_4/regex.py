#  https://www.notion.so/d60d7fed03e844dc87fe63c297d59826
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
        print(first_word.search(word).group())


def task_2():
    two_symbol = re.compile(r'\b\w{2}')
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
        print(two_symbol.findall(word))


def task_3():
    domain_email = re.compile(r'\w+@(\w+\.\w+)')
    e_mails = 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz'
    print(domain_email.findall(e_mails))  # findall ищет только по скобочным группам


def task_4():
    date_str = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
    pattern_date = re.compile(r'(?P<day>\d{2})-(?P<month>\d{2})-(?P<year>\d{4})')
    for date in pattern_date.finditer(date_str):
        print(date.groupdict())
        print(date['day'], '-', date['month'], '-', date['year'])


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
    # task_1()
    # task_2()
    # task_3()
    task_4()

if __name__ == '__main__':
    main()
