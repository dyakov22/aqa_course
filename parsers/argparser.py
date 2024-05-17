import argparse

# parser = argparse.ArgumentParser(description="Test parser")

""" START OF 1 PART """
#
# parser.add_argument("show", help='Just to understand positional arguments')
#
# parser.add_argument("--verbose", "-v", help="Is output verbose", action="store_true")
#
# arguments = parser.parse_args()
#
# print(f"Verbose arg is {arguments.verbose}")
#
# if arguments.verbose:
#     print(f"This is verbose format of output: {arguments.show}")
# else:
#     print(arguments.show)

""" END OF 1 PART """

""" START OF 2 PART """

# parser.add_argument("--integers", "-i", type=int, nargs="+", help="Integers for some programs")
#
# parser.add_argument("--sum", dest="sum_all_ints", action="store_const", const=sum, default=max)
#
# arguments = parser.parse_args()
#
# print(f"Result of execution: {arguments.sum_all_ints(arguments.integers)}")

#  python3 parsers/argparser.py --currency=usd 40 39 28 19

""" END OF 2 PART """
""" START OF 3 PART """

# parser = argparse.ArgumentParser(description="Test parser with groups", prog="AQA Course")
#
# group = parser.add_mutually_exclusive_group()
#
# group.add_argument("--store_true", action="store_true")
# group.add_argument("--store_false", action="store_false")
#
# args = parser.parse_args()
#
# print(f"Store true, {args.store_true}")
# print(f"Store false, {args.store_false}")

""" END OF 3 PART """


#  python3 parsers/argparser.py --currency=usd -40 -39 -28 -19


def check_negative_numbers(number):
    number = int(number)
    if number < 0:
        raise argparse.ArgumentTypeError(f"Expect number is greater than 0, was {number}")
    return number


parser = argparse.ArgumentParser(description="Test parser with callable type")

parser.add_argument("--integer", "-i", action="store", type=check_negative_numbers,
                    help="Check number is greater than 0 ")
parser.add_argument("--verbose", "-v", action="store_true", help="Allow to user get more details in output")

args = parser.parse_args()

# print(args.integer)
"""
Test parser with callable type

options:
  -h, --help            show this help message and exit
  --integer INTEGER, -i INTEGER
                        Check number is greater than 0
  --verbose, -v         Allow to user get more details in output
"""
