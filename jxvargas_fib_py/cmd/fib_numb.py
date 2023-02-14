# Chapter 04: Building pip Modules in Python
# 2. Packaging Python code in a `pip` module
# 2.2 Creating a command-line interface
# 2.2-1 jxvargas_fib_py/cmd/fib_numb.py
import argparse
from jxvargas_fib_py.fib_calcs.fib_number import recurring_fibonacci_number


def fib_numb() -> None:
    """
    Reads from the command line an integer and
    calculates its corresponding Fibonacci number

    :returns: None
    """
    # Here, we can see that we get the parameters
    # passed in from the command line using the
    # argparse module.
    parser = argparse.ArgumentParser(
        description='Calculate Fibonacci numbers'
    )
    parser.add_argument('--number', action='store',
                        type=int, required=True,
                        help='Fibonacci number to be calculated')
    args = parser.parse_args()

    # Once we have obtained the parameters, we will
    # then calculate the number and print it out.
    print(f"Your Fibonacci number is: "
          f"{recurring_fibonacci_number(number=args.number)}")

    # NOTE: Now, for us to actually access it via the terminal,
    # we have to point to it in the setup.py file at the root
    # of the pip package.
    #
    # 	entry_points={
    # 		'console_scripts': [
    # 			'fib-number = jxvargas_fib_py.cmd.fib_numb:fib_numb',
    # 		],
    # 	},