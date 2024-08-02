# recursion.py
# Author: Adam
# Date: August 2, 2024

"""
Description: A collection of recursive functions for common algorithms.
"""
import time

def print_header():
    print("\nMENU OPTIONS")
    print("1 - Calculate and Display Factorial of a Number")
    print("2 - Calculate and Display Fibonacci Series of a Number")
    print("3 - Compare Performance for Factorial Implementations")
    print("4 - Compare Performance for Fibonacci Series Implementations")
    print("0 - EXIT\n")
    choice = int(input("Enter an option (0 to exit): "))
    return choice

def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    if n <= 1:
        return n
    prev1, prev2 = 0, 1
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev1, prev2 = prev2, current
    return prev2

def compare_factorial_performance(n):
    start_recursive = time.time()
    for _ in range(1000):
        factorial_recursive(n)
    end_recursive = time.time()
    duration_recursive = (end_recursive - start_recursive) * 1000000  # Convert to microseconds

    start_iterative = time.time()
    for _ in range(1000):
        factorial_iterative(n)
    end_iterative = time.time()
    duration_iterative = (end_iterative - start_iterative) * 1000000  # Convert to microseconds

    print(f"Recursive factorial execution time: {duration_recursive:.2f} microseconds")
    print(f"Iterative factorial execution time: {duration_iterative:.2f} microseconds")

def compare_fibonacci_performance(n):
    start_recursive = time.time()
    for _ in range(100):
        fibonacci_recursive(n)
    end_recursive = time.time()
    duration_recursive = (end_recursive - start_recursive) * 1000000  # Convert to microseconds

    start_iterative = time.time()
    for _ in range(100):
        fibonacci_iterative(n)
    end_iterative = time.time()
    duration_iterative = (end_iterative - start_iterative) * 1000000  # Convert to microseconds

    print(f"Recursive Fibonacci execution time: {duration_recursive:.2f} microseconds")
    print(f"Iterative Fibonacci execution time: {duration_iterative:.2f} microseconds")

def print_heading():
    PROGRAMMER = "Adam Mirski"
    LAB_NAME = "Recrusion Performance Program"

    heading = "*" * 60 + "\n"
    heading += f"* PROGRAMMED BY : {PROGRAMMER}\n"
    heading += f"* LAB#          : {LAB_NAME}\n"
    heading += "*" * 60

    print(heading)

def main():
    print_heading()

    choice = None
    while choice != 0:
        choice = print_header()

        if choice == 1:
            n = int(input("Enter a number (n) to calculate the factorial: "))
            print(f"Factorial of {n} using recursion: {factorial_recursive(n)}")
        elif choice == 2:
            n = int(input("Enter a number (n) to calculate the Fibonacci Series: "))
            print(f"Fibonacci Series of {n} using recursion: ", end="")
            for i in range(n + 1):
                print(fibonacci_recursive(i), end=" ")
            print()
        elif choice == 3:
            n = int(input("Enter a number (n) to compare factorial performance: "))
            compare_factorial_performance(n)
        elif choice == 4:
            n = int(input("Enter a number (n) to compare Fibonacci Series performance: "))
            compare_fibonacci_performance(n)
        elif choice == 0:
            print("Exiting the program.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

"""
Code Explanation

Here’s a brief explanation of each section of the code:

	1.	Header Comments:

	2.	Factorial Function:
	•	Purpose: Calculates the factorial of a given number  n .
	•	Base Case: If  n  is 0 or 1, return 1.
	•	Recursive Case: Multiply  n  by the factorial of  n-1 .
	3.	Fibonacci Function:
	•	Purpose: Calculates the  n -th Fibonacci number.
	•	Base Cases: Return 0 if  n  is 0 and 1 if  n  is 1.
	•	Recursive Case: Sum the two preceding Fibonacci numbers.
	4.	GCD Function:
	•	Purpose: Calculates the greatest common divisor of two numbers  a  and  b  using the Euclidean algorithm.
	•	Base Case: If  b  is 0, return  a .
	•	Recursive Case: Call gcd with  b  and the remainder of  a  divided by  b .
	5.	Power Function:
	•	Purpose: Calculates  x  raised to the power  n .
	•	Base Case: If  n  is 0, return 1.
	•	Recursive Case: If  n  is negative, return the reciprocal of the positive power. Otherwise, multiply  x  by the power of  x, n-1 .
	6.	Palindrome Check Function:
	•	Purpose: Determines if a given string  s  is a palindrome.
	•	Preprocessing: Filters out non-alphanumeric characters and converts the string to lowercase.
	•	Base Case: A string with less than two characters is a palindrome.
	•	Recursive Case: Compare the first and last characters, then recurse on the substring.
	7.	Binary Search Function:
	•	Purpose: Performs a binary search on a sorted array to find the target element.
	•	Base Case: If the lower index is greater than the upper index, the target is not in the array.
	•	Recursive Case: Calculate the middle index and compare the target with the middle element, then recurse into the appropriate half of the array.
"""
