def perform_calculation():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print('select operation:\n 1.Addition\n 2.Subtarction\n 3.Multiplication\n 4.Divison\n 5.a to the power b ')
    num = int(input("Enter the number of the operation: "))
    if num == 1:
        print("Addition:", a + b)
    elif num == 2:
        print("Subtraction:", a - b)
    elif num == 3:
        print("Multiplication:", a * b)
    elif num == 4:
        if b == 0:
            print("Division by zero is not allowed.")
        else:
            print("Division:", a / b)
    elif num == 5:
        print("a to the power of b:", a ** b)
    else:
        print("Error: Invalid operation selected.")
while True:
    perform_calculation()
    next_calculation = input("Let's do another calculation? (yes/no): ").strip().lower()
    if next_calculation == "no":
        break
    else: 
        next_calculation != "yes"
        print("Invalid input. Please enter 'yes' or 'no'.")
