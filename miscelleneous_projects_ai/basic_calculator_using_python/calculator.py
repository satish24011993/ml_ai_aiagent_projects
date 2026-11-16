# Function to add two numbers
def add(a,b):
    return a+b

# Function to subtract two numbers
def subtract(a,b):
    return a-b

# Function to divide two numbers
def divide(a,b):
    if b == 0:
        return "Error can't divide by 0"
    return a/b

# Function to multiply two numbers
def multiply(a,b):
    return a*b


def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    while True:
        try:
            operation = int(input('Select the operation:').strip())
            a,b = map(int,input('Enter the input values for the operation:').split(','))
            if operation == 1:
                print(add(a,b))
            elif operation == 2:
                print(subtract(a,b))
            elif operation == 3:
                print(multiply(a,b))
            elif operation == 4:
                print(divide(a,b))
        except Exception as e:
            print(e)

if __name__=='__main__':
    calculator()