def get_average(a, b, c):
    return (a + b + c) / 3


flag = None

while flag != 'exit':
    a = int(input('Enter an integer a: '))
    b = int(input('Enter an integer b: '))
    c = int(input('Enter an integer c: '))

    print('Average is:', get_average(a, b, c))
    print('Type "exit" to exit or press "Enter" to continue ')
    flag = input()
