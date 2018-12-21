rows = int(input('Enter number of rows: '))
columns = int(input('Enter number of columns: '))

for i in range(rows, 0, -1):
    for j in range(columns, 0, -1):
        print('*', end='')
    print()
