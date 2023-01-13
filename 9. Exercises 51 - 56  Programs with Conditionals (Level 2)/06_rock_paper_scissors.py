

import random


def menu():
    print('--------------------------------------------')
    print('Rock, Paper, Scissors...   ')
    print('--------------------------------------------')
    print('1 : Rock')
    print('2 : Paper')
    print('3 : Scissors')
    print('q : Quit')
    print('--------------------------------------------')
    return input('Select Option : ')


exit = True


def get_random():
    i = int(random.random() * 10 % 3)
    if i == 0:
        return 'Rock'
    elif i == 1:
        return 'Paper'
    else:
        return 'Scissor'


def get_result(user: str, computer: str):
    if user == computer:
        return 'It\'s a tie, sorry try again...'
    elif user == 'Rock' and computer == 'Scissor':
        return 'You win !!! Your opponent chose scissor...'
    elif (user == 'Rock' and computer == 'Paper'):
        return 'You lose !!! Your opponent chose paper...'
    elif user == 'Paper' and computer == 'Rock':
        return 'You win !!! Your opponent chose rock...'
    elif user == 'Paper' and computer == 'Scissor':
        return 'You lose !!! Your opponent chose scissor...'
    elif user == 'Scissor' and computer == 'Paper':
        return 'You win !!! Your opponent chose scissor...'
    elif user == 'Scissor' and computer == 'Rock':
        return 'You lose !!! Your opponent chose rock...'


while exit:
    option = menu()
    if option.isdigit() and int(option) == 1:
        print('--------------------------------------------')
        print(get_result('Rock', get_random()))
    elif option.isdigit() and int(option) == 2:
        print('--------------------------------------------')
        print(get_result('Paper', get_random()))
    elif option.isdigit() and int(option) == 3:
        print('--------------------------------------------')
        print(get_result('Scissor', get_random()))
    elif option == 'q':
        exit = False
        print('--------------------------------------------')
        print('Thanks for using it...')
        print('-------------------------------------\n')
    else:
        print('--------------------------------------------')
        print('Invalid operation...')
        print('--------------------------------------------')
