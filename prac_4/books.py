import re
import json

books_file = '/Users/nikolaj/PycharmProjects/py_110_for_git/prac_4/books.txt'


def books():
    pattern_books = re.compile(
        r'#{4}\s+(?P<position>\d{1,2})\.\s+\[(?P<book>.*?)\]\((?P<book_url>.*?)\)(?:\s+)?by(?:\s+)?(?P<autor>.*?)('
        r'?:\s+)?\((?P<recommended>.*?)\)(?:\s+)?!\[\]\((?P<cover_url>.*?)\)(?:\s+)?\"(?P<description>.*?)\"',
        re.DOTALL)

    with open(books_file) as f:
        for book in pattern_books.finditer(f.read()):
            a = book.groupdict()
            # list_a = list(a.items())
            # list_a.sort(key=lambda i: i[1], reverse=False)
            # print(list_a)
            with open('books.json', 'a') as f:
                json.dump(a, f, indent=4)

            # print(book['position'], '-', book['book'], '-', book['book_url'], '-', book['autor'], '-',
            # book['recommended'], '-', book['cover_url'], '-', book['description'])


def clear_json(obj='', filename='books.json', indent=4):
    with open(filename, 'w') as f:
        json.dump(obj, f, indent=indent)


def main():
    clear_json()
    books()


if __name__ == '__main__':
    main()
