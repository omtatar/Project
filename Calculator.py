def calculator():
    print("Simple Calculator")
    

    # Prompt the user to choose an operation
    print("Choose the operation you want to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    operation = input("Enter the operation (+, -, *, /): ")
   
    # Prompt the user to input the first number
    num1 = float(input("Enter the first number: "))
    
    # Prompt the user to input the second number
    num2 = float(input("Enter the second number: "))
    
    # Perform the calculation based on the user's choice
    if operation == '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please enter one of +, -, *, /.")

# Run the calculator function
calculator()
