# recursion.py
# Author: Adam Mirski
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

