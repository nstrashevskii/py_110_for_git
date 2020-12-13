import argparse
import random
import json
import re
# import csv
from faker import Faker

BOOKS_TITLE_FILE: str = 'books.txt'
BOOKS_AUTHOR_FILE: str = 'authors.txt'
CONF_FILE: str = 'conf.py'
filename_csv: str = 'books.csv'

pattern_author = re.compile(r'\b[A-Z]\w+\b\s\b[A-Z]\w+\b')
with open(BOOKS_AUTHOR_FILE) as books_author:
    for i in books_author.readlines():
        if re.match(pattern_author, i) is None:
            print(f'в строке {i} ошибка')


def isbn13() -> str:
    """
    :return: Международный стандартный номер книги
    """
    fake = Faker()
    Faker.seed(random.randint(1, 10))
    return fake.isbn13()


def clear_json(obj: str = ''):
    with open(args.f, 'w') as file:
        json.dump(obj, file, indent=args.ind)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', type=int, help='count books')
    parser.add_argument('-s', '--sale', type=str, help='sale: yes or no')
    parser.add_argument('-pk', '--pk', type=int, help='start pk', required=False)
    parser.add_argument('-a', type=int, help='number of authors', required=False)
    subparser = parser.add_subparsers(dest='action', description='save as json or csv, or show')
    save_parser = subparser.add_parser('save')
    save_parser.add_argument('-j', type=str, help='save as json: yes or None', required=False)
    subparser_json = save_parser.add_subparsers(dest='action', description='filename and indent')
    json_parser = subparser_json.add_parser('json')
    json_parser.add_argument('-f', type=str, help='filename', default='books.json', required=False)
    json_parser.add_argument('-ind', type=int, help='indent', required=False)
    save_parser.add_argument('-csv', type=str, help='save as csv: yes or None', required=False)

    return parser


def sale() -> [float, None]:
    """
    :return: размер скидки на книгу
    """
    if args.sale == 'yes':
        discount: [float, None] = random.uniform(0, 100)
    else:
        discount = None
    return discount


def authors() -> int:
    """
    :return: количество авторов книги
    """
    if args.a is None:
        k: int = random.randint(1, 3)
    else:
        k: int = args.a
    return k


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


if __name__ == '__main__':
    parsers = create_parser()
    args = parsers.parse_args()
    clear_json()
    if args.j is None and args.csv is None:
        if args.pk is None:
            for i in range(args.count):
                print(next(books_generator(i + 1)))
        else:
            for i in range(args.count):
                print(next(books_generator(i + args.pk)))
    elif args.j is not None:
        if args.pk is None:
            if args.ind is None:

                for i in range(args.count):
                    with open(args.f, 'a') as f:
                        json.dump(next(books_generator(i + 1)), f, indent=0)
            else:
                for i in range(args.count):
                    with open(args.f, 'a') as f:
                        json.dump(next(books_generator(i + 1)), f, indent=args.ind)
        else:
            if args.ind is None:
                for i in range(args.count):
                    with open(args.f, 'a') as f:
                        json.dump(next(books_generator(i + args.pk)), f, indent=0)
            else:
                for i in range(args.count):
                    with open(args.f, 'a') as f:
                        json.dump(next(books_generator(i + args.pk)), f, indent=args.ind)
    # elif args.csv is not None:
    #     if args.pk is None:
    #         for i in range(args.count):
    #             with open(filename_csv, 'a') as f:
    #                 file_writer = csv.DictWriter(f, delimiter=",", lineterminator="\n")
    #                 file_writer.writerows(next(books_generator(i + 1)))
    #     else:
    #         for i in range(args.count):
    #             with open(filename_csv, 'a') as f:
    #                 file_writer = csv.DictWriter(f, delimiter=",", lineterminator="\n")
    #                 file_writer.writerows(next(books_generator(i+args.pk)))
