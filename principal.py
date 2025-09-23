from menu import cadastrar, listar, menu
print('principal')
clientes = []
while True:
    menu()
    opção = int(input('digite opção:'))
    match opção:
        case 1:
            cadastrar(clientes)
        case 2:
            listar(clientes)
        case 0:
            break
        case _:
            print('opção invalida')
