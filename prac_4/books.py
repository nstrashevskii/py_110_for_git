import re
import json

books_file = '/Users/nikolaj/PycharmProjects/py_110_for_git/prac_4/books.txt'


def books():
    a = []
    pattern_books = re.compile(
        r'#{4}\s+(?P<position>\d{1,2})\.\s+\[(?P<book>.*?)\]\((?P<book_url>.*?)\)(?:\s+)?by(?:\s+)?(?P<autor>.*?)('
        r'?:\s+)?\((?P<recommended>.*?)\)(?:\s+)?!\[\]\((?P<cover_url>.*?)\)(?:\s+)?\"(?P<description>.*?)\"',
        re.DOTALL)

    with open(books_file) as f:
        a = sorted(pattern_books.findall(f.read()), key=lambda i: int(i[0]), reverse=False)
        with open('books.json', 'a') as f:
            json.dump(a, f, indent=4)


def clear_json(obj='', filename='books.json', indent=4):
    with open(filename, 'w') as f:
        json.dump(obj, f, indent=indent)


def main():
    clear_json()
    books()


if __name__ == '__main__':
    main()
