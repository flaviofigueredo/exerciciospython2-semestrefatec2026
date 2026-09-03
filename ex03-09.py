# Exercício 1
def pares():
    for i in range(10, 0, -2):
        print(i, end=' ')
    print('')
    
# Execício 2
def quadrado():
    for i in range (1, 6):
        print(f'{i**2}', end=' ')
    print('')

# Exercício 3
def multiplos():
    n = int(input("Digite um número inteiro: "))
    for i in range (1, 11):
        print(f'|{n} X {i} = {n*i}|')

# Exercício 4
def multiplospositivo():
    termino = False
    while termino == False:
        n = int(input("Digite um número inteiro: "))
        if n <= 0:
            print('Número Inválido')
            termino = True
        if termino == False:
            for i in range (1, 11):
                print(f'|{n} X {i} = {n*i}|')
            termino = True
        else:
            termino = True

# Exercício 5
def somanumeros():
    soma = 0
    lista = []
    for i in range (1,11):
        prossegue = False
        while prossegue == False:
            n = int(input(f'Digite o {i}º Número Inteiro: '))
            if n <= 0:
                print('Número Inválido')
            else:
                prossegue = True
                lista.insert(i-1, n)
                soma += n
    print('Demonstração do cálculo:', end=' ')
    for i in range (0, 10):
        if i == 9:
            print(lista[i], end=' = ')
        else:
            print(lista[i], end=' + ')
    print(soma)

# Exercício 6 (BETA)
def somanumerosantinulo():
    soma = 0
    lista = []
    for i in range (1,11):
        prossegue = False
        while prossegue == False:
            n = int(input(f'Digite o {i}º Número Inteiro: '))
            if n <= 0:
                print('Número Inválido')
            else:
                prossegue = True
                lista.insert(i-1, n)
                soma += n
    print('Demonstração do cálculo:', end=' ')
    for i in range (0, 10):
        if i == 9:
            print(lista[i], end=' = ')
        else:
            print(lista[i], end=' + ')
    print(soma)

# Index
while True:
    print("""Escolha qual exercício deseja acessar:
[1] Mostrar múmeros pares de 10 a 0
[2] Exibir o Quadrado de 1 a 5
[3] Exibir 10 primeiros multiplos de um número digitado pelo usuário
[4] Exibir 10 primeiros multiplos de um número digitado pelo usuário, porém deve ser obrigatóriamente positivo, senão não irá executar
[5] Exibir a Soma de 10 números obrigatóriamente positivos que serão digitados pelo usuário, caso não seja cumprido, terá a repetição da ação
[6] Exibir a Soma de 10 números obrigatóriamente positivos que serão digitados pelo usuário, caso seja negativo a ação se repetirá, porém se for igual a 0, o código inteiro para""")
    o = int(input('Digite a opção que deseja: '))
    if o == 2:
        quadrado()
    elif o == 1:
        pares()
    else:
        if o == 3:
            multiplos()
        elif o == 4:
            multiplospositivo()
        else:
            if o == 5:
                somanumeros()
            elif o == 6:
                somanumerosantinulo()
            else:
                print('Digite corretamente')
    op = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if op == 'S':
        print('Continuando...')
    elif op == 'N':
        print('Finalizando...')
        break
    else:
        print('Digite corretamente')

print('Fim do código, tchauu')
