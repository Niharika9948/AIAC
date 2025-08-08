def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

if __name__ == "__main__":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        print(f"Result: {add(x, y)}")
    elif choice == '2':
        print(f"Result: {subtract(x, y)}")
    elif choice == '3':
        print(f"Result: {multiply(x, y)}")
    elif choice == '4':
        print(f"Result: {divide(x, y)}")
    else:
        print("Invalid choice")