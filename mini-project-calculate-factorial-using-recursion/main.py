def factorial(n):
    # Base condition: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive return: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

result = factorial(5)
print("The factorial of 5 is:", result)