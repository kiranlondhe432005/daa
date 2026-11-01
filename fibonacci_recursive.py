# Program to calculate Fibonacci number using Recursive method

def fibonacci_recursive(n):
    # Base condition
    if n <= 0:
        return "Please enter a positive integer"

    if n == 1:
        return 0

    if n == 2:
        return 1

    # Recursive function calls
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Main program
n = int(input("Enter the value of n: "))
result = fibonacci_recursive(n)

print("Fibonacci Number (Recursive):", result)
