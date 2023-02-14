# Chapter 04: Building pip Modules in Python
# 2. Packaging Python code in a `pip` module
# 2.1 Building our Fibonacci calculation code
# 2.1-1 fib_number.py
from typing import Optional

def recurring_fibonacci_number(number: int) -> Optional[int]:
    """
    Calculates the fibonacci number needed.

    :param number: (int) the Fibonacci number to be calculated

    :return: (Optional[int]) the calculated fibonacci number
    """

    # Here, it has to be noted that we are returning None
    # when the input number is below zero.
    # Technically, we should be throwing an error, but this
    # is in place, for now, to demonstrate the effectiveness
    # of a checking tool later on in our 'Configuring continuous
    # integration section'.
    if number < 0:
        return None
    elif number <= 1:
        return number
    else:
        return recurring_fibonacci_number(number - 1) + \
               recurring_fibonacci_number(number - 2)
