# Exercício 1
def criamedia():

    def calculamedia(a, b):
        m = (a+b) / 2
        return m

    a = float(input('Digite a Primeira Nota: '))
    b = float(input('Digite a Primeira Nota: '))
    media = calculamedia(a, b)
    print(f'A sua média foi {media}')

# Exercício 2
def criavalida():

    def validanota(a):
        if a <= 10 and a >= 0:
            return True
        else:
            return False
    
    n = float(input('Digite uma nota: '))
    validacao = validanota(n)
    if validacao == True:
        print('NOTA VÁLIDA')
    else:
        print('NOTA INVÁLIDA')

# Exercício 3
def media():

    def calculamedia(a, b):
        m = (a+b) / 2
        return m
    
    def validanota(a):
        if a <= 10 and a >= 0:
            return True
        else:
            return False 

    print('/'*30)
    print('CALCULADORA DE MÉDIA')
    print('/'*30)

    validacao = False
    while validacao == False:
        a1 = float(input('Digite a primeira nota: '))
        validacao = validanota(a1)
        if validacao == False:
            print('Nota Inválida')

    validacao = False
    while validacao == False:
        a2 = float(input('Digite a segunda nota: '))
        validacao = validanota(a2)
        if validacao == False:
            print('Nota Inválida')

    media = calculamedia(a1, a2)
    print(f'A média do estudante é igual a {media}')
    if media >= 6:
        print('APROVADO')
    else:
        print('REALIZAR SUBSTITUTIVA')
        if a1 > a2:
            menor = a2
        elif a1 < a2:
            menor = a1
        else:
            menor = a1
        nec = ((6-media)*2) + menor
        print(f'A nota necessária para passar é {nec}')

        if nec <= 10:
            validacao = False
            while validacao == False:
                a3 = float(input('Digite a nota da prova substitutiva: '))
                validacao = validanota(a3)
                if validacao == False:
                    print('Nota Inválida')

            if menor == a1:
                nmedia = calculamedia(a2, a3)
            elif menor == a2:
                nmedia = calculamedia(a1, a3)
            else:
                nmedia = calculamedia(a1, a3)

            print(f'A média do estudante é igual a {nmedia}')
            if nmedia >= 6:
                print('APROVADO')
            else:
                print('REPROVADO')
        else:
            print('REPROVADO')
            
# Index
while True:
    print("""Escolha qual exercício deseja acessar:
[1] Criar função Calcular média
[2] Criar função de Validar Nota
[3] Aprimorar o Exercício de Média do dia 27/08 aplicando os dois exercícios anteriores""")
    o = int(input('Digite a opção que deseja: '))
    if o == 1:
        criamedia()
    elif o == 2:
        criavalida()
    else:
        if o == 3:
            media()
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