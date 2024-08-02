
# Recursion Functions

This repository contains a Python script that implements various recursive functions to perform common mathematical and algorithmic tasks. The functions include calculations for factorials, Fibonacci numbers, the greatest common divisor (GCD), list summation, palindrome checks, power calculations, and binary search operations.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Function Descriptions](#function-descriptions)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Factorial Calculation**: Computes the factorial of a given number.
- **Fibonacci Sequence**: Generates the nth Fibonacci number.
- **Greatest Common Divisor**: Finds the GCD of two numbers.
- **List Summation**: Calculates the sum of all elements in a list.
- **Palindrome Check**: Determines if a given string is a palindrome.
- **Power Calculation**: Raises a base number to a specified exponent.
- **Binary Search**: Searches for a target value within a sorted list.

## Installation

To run this script, you need to have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

1. Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/your-username/recursion-functions.git
   ```

2. Navigate to the project directory:

   ```bash
   cd recursion-functions
   ```

3. Run the script:

   ```bash
   python recursion.py
   ```

## Usage

You can use this script to perform a variety of recursive calculations. The script is designed to be easy to use and modify for different purposes. To use a specific function, simply call it with the appropriate arguments as shown in the examples below.

## Function Descriptions

### `factorial(n)`

Calculates the factorial of a non-negative integer `n`.

### `fibonacci(n)`

Generates the nth Fibonacci number, where `n` is a non-negative integer.

### `gcd(a, b)`

Finds the greatest common divisor of two integers `a` and `b`.

### `sum_of_list(lst)`

Calculates the sum of all elements in the list `lst`.

### `is_palindrome(s)`

Checks whether the string `s` is a palindrome.

### `power(base, exp)`

Calculates the result of raising `base` to the power of `exp`.

### `binary_search(arr, target, low, high)`

Performs a binary search to find the `target` in the sorted list `arr` within the indices `low` and `high`.

## Examples

Here's how you can use the functions in the script:

```python
from recursion import factorial, fibonacci, gcd, sum_of_list, is_palindrome, power, binary_search

# Calculate the factorial of 5
print(f"Factorial of 5: {factorial(5)}")  # Output: 120

# Calculate the 5th Fibonacci number
print(f"Fibonacci of 5: {fibonacci(5)}")  # Output: 5

# Calculate the GCD of 48 and 18
print(f"GCD of 48 and 18: {gcd(48, 18)}")  # Output: 6

# Calculate the sum of the list [1, 2, 3, 4, 5]
print(f"Sum of list [1, 2, 3, 4, 5]: {sum_of_list([1, 2, 3, 4, 5])}")  # Output: 15

# Check if 'radar' is a palindrome
print(f"Is 'radar' a palindrome? {is_palindrome('radar')}")  # Output: True

# Calculate 2 raised to the power of 3
print(f"2 to the power of 3: {power(2, 3)}")  # Output: 8

# Perform a binary search for 3 in the sorted list [1, 2, 3, 4, 5]
print(f"Binary search for 3 in [1, 2, 3, 4, 5]: {binary_search([1, 2, 3, 4, 5], 3, 0, 4)}")  # Output: 2
```

