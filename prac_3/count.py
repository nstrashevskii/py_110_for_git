import argparse


def count(start, step):
    current_value = start
    while True:
        new_start = yield current_value
        if new_start is None:
            current_value += step
        else:
            current_value = new_start


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('start', )
    parser.add_argument('step', )
    parser.add_argument('-n', )

    subparser = parser.add_subparsers(dest='action', description='wiwesti d consol ili v fail')

    create_save_subparser(subparser)
    create_show_subparser(subparser)

    return parser


def create_save_subparser(subparser):
   parser = subparser.add_parser('save')


def create_show_subparser(subparser):
   parser = subparser.add_parser('show')


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.action == 'show':
        # печатаем в консоль
        ...
    elif args.action == 'save':
        # сохраняем в файл
        ...


if __name__ == '__main__':
    main()
