from time import sleep

# Exercício 1
def parimpar():
    while True:
        num = int(input('Digite um número: '))
        if num <= 0:
            sleep(0.5)
            print('Número Inválido, digite o número novamente')
            sleep(0.5)
        else:
            sleep(0.5)
            break
    if num % 2 == 0:
        print(f'{num} é um número par')
    else:
        print(f'{num} é um número ímpar')

# Exercício 2
def imc():
    while True:
        peso = float(input('Digite o seu peso: '))
        if peso <= 0:
            print('Peso Inválido')
        else:
            break
    sleep(0.5)
    while True:
        altura = float(input('Digite a sua altura: '))
        if altura <= 0:
            print('Altura Inválida')
        else:
            break
    sleep(0.5)
    im = peso / (altura ** 2)
    if im < 18.5:
        print(f'Seu IMC é de {im}, na qual se classifica como "ABAIXO DO PESO"')
    else:
        if im > 30:
            print(f'Seu IMC é de {im}, na qual se classifica como "OBESIDADE"')
        elif 25 <= im <= 29.9:
            print(f'Seu IMC é de {im}, na qual se classifica como "SOBREPESO"')
        else:
            print(f'Seu IMC é de {im}, na qual se classifica como "PESO NORMAL"')

# Exercício 3
def media():
    print('/'*30)
    print('CALCULADORA DE MÉDIA')
    print('/'*30)
    while True:
        a1 = float(input('Digite a primeira nota: '))
        if a1 < 0 or a1 > 10:
            print('Nota Inválida')
        else: 
            break
    while True:
        a2 = float(input('Digite a segunda nota: '))
        if a2 < 0 or a2 > 10:
            print('Nota Inválida')
        else: 
            break
    media = (a1+a2)/2
    sleep(0.5)
    print(f'A média do estudante é igual a {media}')
    sleep(0.5)
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
        sleep(0.5)
        print(f'A nota necessária para passar é {nec}')
        sleep(0.5)
        while True:
            if nec > 10:
                print('REPROVADO')
                break
            while True:
                a3 = float(input('Digite a nota da prova substitutiva: '))
                if a3 < 0:
                    print('Nota Inválida')
                else: 
                    break
            sleep(0.5)
            if menor == a1:
                nmedia = (a2+a3)/2
            elif menor == a2:
                nmedia = (a1+a3)/2
            else:
                nmedia = (a1+a3)/2
            sleep(0.5)
            print(f'A média do estudante é igual a {nmedia}')
            sleep(0.5)
            if nmedia >= 6:
                print('APROVADO')
                break
            else:
                print('REPROVADO')
                break

# Index
while True:
    print("""Escolha qual exércicio deseja acessar:
[1] Par ou ímpar
[2] Calculadora de IMC
[3] Cálculo de Média do Estudante""")
    o = int(input('Digite a opção que deseja: '))
    if o == 2:
        imc()
    elif o == 1:
        parimpar()
    else:
        if o == 3:
            media()
        else:
            print('Digite corretamente')
    op = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if op == 'S':
        sleep(0.5)
        print('Continuando...')
    elif op == 'N':
        sleep(0.5)
        print('Finalizando...')
        break
    else:
        sleep(0.5)
        print('Digite corretamente')

sleep(0.5)
print('Fim do código, tchauu')
