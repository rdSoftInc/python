

def menu():
    print('-------------------------------------')
    print('Basic Calculator...   ')
    print('-------------------------------------')
    print('1 : Addition')
    print('2 : Subtraction')
    print('3 : Multiplication')
    print('4 : Division')
    print('5 : Integer Division')
    print('6 : Modulus')
    print('q : Quit')
    print('-------------------------------------')
    return input('Select Option : ')


exit = True


while exit:
    option = menu()
    if option.isdigit() and int(option) == 1:
        print('-------------------------------------')
        x = int(input('Enter First Number : '))
        print('-------------------------------------')
        y = int(input('Enter Second Number : '))
        print('-------------------------------------')
        print('Addition : ' + str(int(x+y)))
        print('-------------------------------------')
    elif option.isdigit() and int(option) == 2:
        print('-------------------------------------')
        x = int(input('Enter First Number : '))
        print('-------------------------------------')
        y = int(input('Enter Second Number : '))
        print('-------------------------------------')
        print('Substraction : ' + str(int(x-y)))
        print('-------------------------------------')
    elif option.isdigit() and int(option) == 3:
        print('-------------------------------------')
        x = int(input('Enter First Number : '))
        print('-------------------------------------')
        y = int(input('Enter Second Number : '))
        print('-------------------------------------')
        print('Multiplication : ' + str(int(x*y)))
        print('-------------------------------------')
    elif option.isdigit() and int(option) == 4:
        print('-------------------------------------')
        x = int(input('Enter First Number : '))
        print('-------------------------------------')
        y = int(input('Enter Second Number : '))
        print('-------------------------------------')
        if y == 0:
            print('Cannot Divide By Zero...')
        else:
            print('Division : ' + str(int(x/y)))
            print('-------------------------------------')
    elif option.isdigit() and int(option) == 5:
        print('-------------------------------------')
        x = int(input('Enter First Number : '))
        print('-------------------------------------')
        y = int(input('Enter Second Number : '))
        print('-------------------------------------')
        if y == 0:
            print('Cannot Divide By Zero...')
        else:
            print('Integer Division : ' + str(int(x//y)))
            print('-------------------------------------')
    elif option.isdigit() and int(option) == 6:
        print('-------------------------------------')
        x = int(input('Enter First Number : '))
        print('-------------------------------------')
        y = int(input('Enter Second Number : '))
        print('-------------------------------------')
        print('Modulus : ' + str(int(x % y)))
        print('-------------------------------------')
    elif option == 'q':
        exit = False
        print('-------------------------------------')
        print('Thanks for using it...')
        print('-------------------------------------\n')
    else:
        print('-------------------------------------')
        print('Invalid operation...')
        print('-------------------------------------')
