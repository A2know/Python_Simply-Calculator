def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiplication(num1,num2):
    return num1 * num2

def division(num1,num2):
    if num2 != 0:
        result = round(num1/num2,3)
    else:
        print('Error: Division by 0 !')
        return None
    return result

def modulo(num1,num2):
    if num2 != 0:
        result = num1%num2
    else:
        print('Error: Division by 0 !')
        return None
    return result

def exponentiation(num1,num2):
    return num1**num2

while True:
    print('...:Calc:....')
    print('[1] Addition')
    print('[2] Subtract')
    print('[3] Multiplication')
    print('[4] Division')
    print('[5] Modulo')
    print('[6] Exponentiation')
    print('[q] Quit')

    select = input('Chose math operation: ')


    if select == '1':
        number_1 = float(input('Enter first number: '))
        number_2 = float(input('Enter second number: '))
        print(f'{number_1} + {number_2} = {add(number_1,number_2)}')
        break
    elif select == '2':
        number_1 = float(input('Enter first number: '))
        number_2 = float(input('Enter second number: '))
        print(f'{number_1} - {number_2} = {subtract(number_1, number_2)}')
        break
    elif select == '3':
        number_1 = float(input('Enter first number: '))
        number_2 = float(input('Enter second number: '))
        print(f'{number_1} * {number_2} = {multiplication(number_1, number_2)}')
        break
    elif select == '4':
        number_1 = float(input('Enter first number: '))
        number_2 = float(input('Enter second number: '))
        print(f'{number_1} / {number_2} = {division(number_1, number_2)}')
        break
    elif select == '5':
        number_1 = float(input('Enter first number: '))
        number_2 = float(input('Enter second number: '))
        print(f'{number_1} % {number_2} = {modulo(number_1, number_2)}')
        break
    elif select == '6':
        number_1 = float(input('Enter first number: '))
        number_2 = float(input('Enter second number: '))
        print(print(f'{number_1} ^ {number_2} = {exponentiation(number_1, number_2)}'))
        break
    elif select.lower() == 'q':
        print('Quite calc')
        exit(0)
    else:
        print('This didn\'t look like a number, try again.')

