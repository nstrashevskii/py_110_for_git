import sys
import os


def main():
    path_to_script = sys.argv[0]
    dirname = os.path.dirname(path_to_script)
    filename = os.path.basename(path_to_script)
    print(dirname)
    print(filename)


if __name__ == '__main__':

    main()