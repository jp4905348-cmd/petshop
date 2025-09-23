def menu(): #implementando a função
    print('menu')
    print('1 - cadastro')
    print('2 - listar')
    print('0 - sair')

menu() #chamando a função
menu()

def cadastrar(lista):
    while True:
        pessoa = {}
        nome = input('informe o nome:')
        idade = int(input('informe a idade:'))
        pessoa['nome'] = nome
        pessoa['idade'] = idade
        pessoa['animais'] = cadastrarPet()
        lista.append(pessoa)
        r = pegarResposta('deseja cadastrar outro cliente?')
        if r == True:
            break
def cadastrarPet():
    animais = []
    while True:
        nome = input('informe o nome do seu animal:')
        animais.append(nome)
        r = pegarResposta('deseja cadastrar outro animal')
        if r == True:
            break
    return animais
def pegarResposta(frase):
    retorno = False
    while True:
        r = input(f'{frase}? (s/n)')
        r = r[0].lower()
        if r != 's' and r != 'n':
            print('Resposta invalida')
        else:
            break
    if r == 'n':
        retorno = True
    return retorno
def listar(lista):
    for elemento in lista:
        print(f'{elemento["nome"]} - {elemento["idade"]}')
        print('os pets:')
        for pet in elemento['animais']:
            print(pet)
        print("-"*30)
    
