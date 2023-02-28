def add(x, y):
    return x + y

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter a number.")

print(num1, "+", num2, "=", add(num1, num2))