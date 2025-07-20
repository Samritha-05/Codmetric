def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


while True:
    print("\n***SIMPLE CALCULATOR***")
    print("Choose an Arithmetic operation:")
    print("1. ADDITION (+)")
    print("2. SUBTRACTION (-)")
    print("3. MULTIPLICATION (*)")
    print("4. DIVISION (/)")
    
    choice = input("Enter your choice: ")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            result = add(num1, num2)
            operator = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operator = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operator = '*'
        elif choice == '4':
            if num2 == 0:
                raise ZeroDivisionError
            result = divide(num1, num2)
            operator = '/'
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
            continue

        print(f"\nResult: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("Invalid input! Please enter numbers only.")
    except ZeroDivisionError:
        print("Warning!! Division by zero is not allowed!")

    
    again = input("\nDo you want to calculate again?: ").lower()
    if again != 'yes':
        print("------------------------------------------")
        break

        
