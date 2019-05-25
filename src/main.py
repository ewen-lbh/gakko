import sys

from src.wizards import schedule


def main(args):
    if args.command == 'configure':
        schedule.main()

    else:
        print("Not supported yet.")
        sys.exit()