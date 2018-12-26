def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        print('Cannot divide by zero!')


flag = None

while flag != 'exit':
    a = int(input('Enter a: '))
    math_sign = input('Input math symbol: ')
    b = int(input('Enter b: '))
    if math_sign == '+':
        print(a, '+', b, '=', addition(a, b))
    elif math_sign == '-':
        print(a, '-', b, '=', subtraction(a, b))
    elif math_sign == '*':
        print(a, '*', b, '=', multiplication(a, b))
    elif math_sign == '/':
        print(a, '/', b, '=', division(a, b))
    else:
        print('Please enter valid math symbol ( + - * / )')

    print('Type "exit" to exit or press "Enter" to continue ')
    flag = input()
