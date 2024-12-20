def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def fibonacci_app():
    try:
        n = int(input("Enter the number of Fibonacci terms you want: "))
        if n <= 0:
            print("Please enter a positive number.")
        else:
            print(f"The first {n} Fibonacci numbers are:")
            print(fibonacci_sequence(n))
    except ValueError:
        print("Invalid input! Please enter a valid number.")

fibonacci_app()
