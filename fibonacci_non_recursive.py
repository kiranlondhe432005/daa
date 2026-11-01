# Program to calculate Fibonacci number using Non-Recursive method

def fibonacci_non_recursive(n):
    if n <= 0:
        return "Please enter a positive integer"

    if n == 1:
        return 0

    if n == 2:
        return 1

    # Initialize an array
    dp = [0] * n

    # First two Fibonacci numbers
    dp[0] = 0
    dp[1] = 1

    # Calculate remaining Fibonacci numbers
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n - 1]


# Main program
n = int(input("Enter the value of n: "))
result = fibonacci_non_recursive(n)

print("Fibonacci Number (Non-Recursive):", result)
