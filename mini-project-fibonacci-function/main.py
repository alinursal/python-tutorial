def fibonacci(n):
    # Base conditions: Fibonacci of 0 is 0 and Fibonacci of 1 is 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive return: Fibonacci of n is the sum of Fibonacci of (n-1) and Fibonacci of (n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

result = fibonacci(6)
print("The 6th Fibonacci number is:", result)