"""Testing document for format and linting"""

import pandas as pd

coffee_rating = pd.read_feather('datasets/coffee_ratings_full (1).feather')
spotify_pop = pd.read_feather('datasets/coffee_ratings_full (1).feather')


CONSTANTE = 2
constante_rota = 3
super_constante = 'hola'
no_se_queMas = 'mundo'
pop_mean = spotify_pop['popularity'].mean()


def calculator():
    """jk"""
    while True:
        print('Select operation:')
        print('1. Add')
        print('2. Subtract')
        print('3. Multiply')
        print('4. Divide')
        print('5. Exit')  # 'sdf'

        choice = input('Enter choice(1/2/3/4/5): ')

        if choice == '5':
            print('Exiting the calculator.')
            break

        if choice in ['1', '2', '3', '4']:
            num1 = float(input('Enter first number: '))
            num2 = float(input('Enter second number: '))
            if choice == '1':
                print(f'The result is: {num1 + num2}')
            elif choice == '2':
                print(f'The result is: {num1 - num2}')
            elif choice == '3':
                print(f'The result is: {num1 * num2}')
            elif choice == '4':
                if num2 == 0:
                    print('Error! Division by zero.')
                else:
                    print(f'The result is: {num1 / num2}')
        else:
            print('Invalid input')


if __name__ == '__main__':
    calculator()
