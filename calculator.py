def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def to_the_power_off(x, y):
    return x**y

def divide(x, y):
    if y!=0:
        return x/y
    else:
        return("Can't divide by 0")
    

while True:
    num1 =float((input("Enter the first number \n")))
    if input == str:
        print('Helytelen formátum')
    
    
    num2 = float(input("Enter the second number \n"))
    operation = input("Enter the operation (+, -, *, **, /):\nor ype 'exit' to close program\n" )

    result = 0

    if operation == "+":
        result = add(num1, num2)

    if operation == '-':
        result = subtract(num1, num2)

    if operation == '*':
        result = multiply(num1, num2)

    if operation == '**':
        result = to_the_power_off(num1, num2)

    if operation == '/':
        result = divide(num1, num2)

    if operation == 'exit':
        break

    print(result)


