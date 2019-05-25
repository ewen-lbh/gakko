import argparse

from src import main

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Complete school management system for students')

    parser.add_argument('command', metavar='COMMAND', type=str, nargs=1,
                        help="Commands: configure, run")

    args = parser.parse_args()

    main.main(args)