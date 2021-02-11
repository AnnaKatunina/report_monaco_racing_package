import argparse

from report_app import print_report


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", type=str, help='path to the folder')
    parser.add_argument("--asc", help='ascending order', action='store_true')
    parser.add_argument("--desc", help='descending order', action='store_true')
    parser.add_argument("--driver", type=str, help='full name of driver', nargs=2)
    args = parser.parse_args()
    if args.files and args.desc:
        print_report(args.files, order='desc')
    elif args.files and args.driver:
        print_report(args.files, driver=' '.join(args.driver))
    else:
        print_report(args.files)


if __name__ == '__main__':
    parse()
