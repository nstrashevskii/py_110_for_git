import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=argparse.FileType(mode='rt'), help='file name')
    parser.add_argument('-n', type=int, help='kollichestvo strok', default=3)

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    for _ in range(args.n):
        print(next(args.filename))


if __name__ == '__main__':
    main()