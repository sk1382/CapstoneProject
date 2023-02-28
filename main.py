from subtraction import subtract
from addition import add
from multiplication import multiply
from division import div
from square import square

while True:
    choice = input("1. Add\n2. Subtract\n3. Multiplicaiton\n4. Division \n5. Exit\nEnter you choice:")
    num1 = int(input("Num1: "))
    num2 = int(input("Num2: "))
    if choice == "1":
        print(add(num1, num2))
    elif choice == "2":
        print(subtract(num1, num2))
    elif choice == "3":
        print(multiply(num1, num2))
    elif choice == "4":
        print(div(num1, num2))
    elif choice == "5":
        print("Thanks for using our basic calculator:).")
        break
    else:
        print()
