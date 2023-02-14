# Chapter 04: Building pip Modules in Python
# 2. Packaging Python code in a `pip` module
# 2.1 Building our Fibonacci calculation code
# 2.1-2 fib_numbers.py
from .fib_number import recurring_fibonacci_number

# Now that we have the `recurring_fibonacci_number` function,
# we can depend on this to create a function that creates a
# list of Fibonacci numbers in our fib_numbers.py file with
# the following code:
def calculate_numbers(numbers: list[int]) -> list[int]:
    """
    Calculates a range of Fibonacci numbers from a list.

    :param numbers: (list[int]) the Fibonacci numbers to be calculated
    :return: (list[int]) the calculated Fibonacci numbers
    """
    return [recurring_fibonacci_number(number=i)
            for i in numbers]
