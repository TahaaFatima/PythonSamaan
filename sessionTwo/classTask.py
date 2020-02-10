firstNumber = float(input('Enter the first number : '))
secondNumber = float(input('Enter the second number : '))
operation = input('Enter the operation : add, sub, mult, div or operation symbol : ').strip()
if operation == 'add' or operation == '+':
    print(f'Addition = {firstNumber + secondNumber}')
elif operation == 'sub' or operation == '-':
    print(f'Subtraction = {firstNumber - secondNumber}')
elif operation == 'mult' or operation == '*':
    print(f'Multiplication = {firstNumber * secondNumber}')
elif operation == 'div' or operation == '/':
    print(f'Division = {firstNumber / secondNumber}')
else:
    print('Operator not found')