import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=argparse.FileType(mode='rt'), help='file name')

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    count = 0
    for _ in args.filename:
        count += 1
    print(count)


if __name__ == '__main__':
    main()