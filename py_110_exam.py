import argparse
import random
import json
import re
from faker import Faker

BOOKS_TITLE_FILE: str = 'books.txt'
BOOKS_AUTHOR_FILE: str = 'authors.txt'
CONF_FILE: str = 'conf.py'


def authors_check():
    pattern_author = re.compile(r'\b[A-Z]\w+\b\s\b[A-Z]\w+\b')
    with open(BOOKS_AUTHOR_FILE) as books_author:
        for i in books_author.readlines():
            if re.match(pattern_author, i) is None:
                yield i


def isbn13() -> str:
    """
    :return: Международный стандартный номер книги
    """
    fake = Faker()
    Faker.seed(random.randint(1, 10))
    return fake.isbn13()


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', type=int, help='count books', default=1)
    parser.add_argument('-s', '--sale', type=str, default='yes', help='sale: yes or no')
    parser.add_argument('-pk', '--pk', type=int, help='start pk', default=1, required=False)
    parser.add_argument('-a', type=int, help='number of authors', default=2, required=False)

    subparser = parser.add_subparsers(dest='action', description='save as json or show')

    save_parser = subparser.add_parser('save')
    save_parser.add_argument('-f', type=str, help='filename', default='books.json', required=False)
    save_parser.add_argument('-ind', type=int, help='indent', default=0, required=False)

    show_parser = subparser.add_parser('show')

    return parser


def arguments() -> [int, str]:
    parsers = create_parser()
    args = parsers.parse_args()
    return args


def clear_json(obj: str = ''):
    args = arguments()
    with open(args.f, 'w') as file:
        json.dump(obj, file, indent=args.ind)


def sale() -> [float, None]:
    """
    :return: размер скидки на книгу
    """
    discount: [float, None] = random.uniform(0, 100)
    return discount if arguments().sale == 'yes' else None


def authors() -> int:
    """
    :return: количество авторов книги
    """
    args = arguments()
    return random.randint(1, 3) if args.a is None else arguments().a


def books_generator(pk: int) -> dict:
    """
    :param pk: счетчик книг
    :return: информация по книгам
    """
    year: int = random.randint(1800, 2020)
    pages: int = random.randint(1, 100)
    rating: int = random.randint(1, 100)
    price: float = random.uniform(1, 10000)
    author: list = []
    pattern_authors = re.compile(r'\b[A-Z]\w+\b\s\b[A-Z]\w+\b')
    with open(CONF_FILE) as conf:
        model = conf.readline()
    with open(BOOKS_TITLE_FILE) as books_title:
        for _ in range(pk):
            title: str = books_title.readline()
    with open(BOOKS_AUTHOR_FILE) as books_authors:
        a = pattern_authors.findall(books_authors.read())
        for j in range(authors()):
            author.append(a[j])
    book = {
        "model": model,
        "pk": pk,
        "fields": {
            "title": title,
            "year": year,
            "pages": pages,
            "isbn13": isbn13(),
            "rating": rating,
            "price": price,
            "discount": sale(),
            "author": author
        }
    }
    yield book


def main():
    args = arguments()
    for i in range(args.a):
        print('ошибка в файле с авторами', next(authors_check()))
    if args.action is None or args.action == 'show':
        for i in range(args.count):
            print(next(books_generator(i + args.pk)))
    else:
        clear_json()
        for i in range(args.count):
            with open(args.f, 'a') as f:
                json.dump(next(books_generator(i + args.pk)), f, indent=args.ind)


if __name__ == '__main__':
    main()

