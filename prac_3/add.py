import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('a', type=int, help='wwedite pervii argument')
    parser.add_argument('b', type=int, help='wwedite wtoroi argument')

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    print(args.a + args.b)


if __name__ == '__main__':
    main()