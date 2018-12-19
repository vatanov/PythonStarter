import math

math_oper = input('''Select math operation:
1. addition
2. subtraction
3. multiplication
4. division
5. exponentiation
6. sinus
7. cosine
8. tangent \n''')

if math_oper == '1' or math_oper == '2' or math_oper == '3' or math_oper == '4':
    a = float(input('Enter first number: '))
    b = float(input('Enter second number: '))
    if math_oper == '1':
        print(a, '+', b, '=', a + b)
    elif math_oper == '2':
        print(a, '-', b, '=', a - b)
    elif math_oper == '3':
        print(a, '*', b, '=', a * b)
    elif math_oper == '4':
        if b == 0:
            print('Cannot divide by zero!')
        else:
            print(a, '/', b, '=', a / b)
elif math_oper == '5':
    a = float(input('Enter number: '))
    b = float(input('Enter exponent: '))
    print(a, 'in exponent', b, '=', a ** b)
elif math_oper == '6' or math_oper == '7' or math_oper == '8':
    a = float(input('Enter number: '))
    if math_oper == '6':
        print('sinus', a, '=', math.sin(a))
    elif math_oper == '7':
        print('cosine', a, '=', math.cos(a))
    elif math_oper == '8':
        print('tangent', a, '=', math.tan(a))
