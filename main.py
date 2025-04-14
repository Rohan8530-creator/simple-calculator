def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

if __name__ == "__main__":
    x = 10
    y = 5

    print(f"Addition of {x} and {y}: {add(x, y)}")
    print(f"Subtraction of {x} and {y}: {subtract(x, y)}")
    print(f"Multiplication of {x} and {y}: {multiply(x, y)}")
    print(f"Division of {x} and {y}: {divide(x, y)}")
