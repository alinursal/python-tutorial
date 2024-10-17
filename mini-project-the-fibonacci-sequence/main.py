def main():
    count = int(input("Enter the number of Fibonacci terms to print: "))
    a, b = 0, 1
    print("Fibonacci sequence:")
    for _ in range(count):
        print(a, end=" ")
        a, b = b, a + b 
main()