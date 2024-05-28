#Function to add 2 numbers

def add(x,y):
    return x + y

#Function to Subtract 2 Numbers

def subtract(x,y):
    return x - y

#Function to Multiply 2 Numbers

def multiply(x,y):
    return x * y

#Function to Divide 2 Numbers

def divide(x,y):
    return x / y 

print("Select Operation")
print('1. Add')
print('2. substract')
print('3. multiply')
print('4. divide')

while True:
#Take input from user
    choice = input("Enter Choice (1/2/3/4):")

# Check if choice is one of the answer
    if choice in ('1' , '2' , '3' , '4'):
        try:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter the Second Number: "))
        except ValueError:
            print("Wrong Value, Please Enter a Number.")
            continue

        if choice == '1':
            print(num1, '+', num2, '=', add(num1,num2))
        elif choice == '2':
            print(num1, '-', num2, '=', subtract(num1,num2))
        elif choice == '3':
            print(num1, '*', num2, '=', multiply(num1,num2))
        elif choice == '4':
            print(num1, '/', num2, '=', divide(num1,num2))

        next_calculation = input("Let's do the next calculation? (Y/N): ")
        if next_calculation == "no":
            break
    else:
            print("Invalid input")
