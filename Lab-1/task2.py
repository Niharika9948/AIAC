def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Example usage:
n = int(input("Enter the number of terms: "))
print("Fibonacci series up to", n, "terms:")
print(fibonacci_series(n))