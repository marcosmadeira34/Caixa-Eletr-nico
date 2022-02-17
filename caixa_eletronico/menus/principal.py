from . import admin, users
from getpass import getpass

def menu_principal():
    select = {
        'L': 'Fazer Login',
        'S': 'Sair e encerrar programa'
    }

    while True:
        print()
        print('='* 10, 'MENU PRINCIPAL', '='*10)
        print('Sejam Bem-Vindos ao Caixa Eletrônico. Selecione uma opção para continuar.')

        for (op, desc) in select.items():
            print(f'{op} - {desc}')

        options = input('Opção: ').strip().upper()

        if options == "L":
            username = input('Username: ')
            password = getpass('Password: ')

            if 'Admin User':
                admin.menu_admin()

            if 'Client User':
                users.menu_users()

        elif options == "S":
            print("Obrigado por usar nosso sistema. Até logo!")
            break

        else:
            print('Por favor, entre com uma opção válida..')