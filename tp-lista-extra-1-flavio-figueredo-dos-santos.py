# Exercício 1 ---------------------------------------------------------------
def inserir():
    continua = False
    while continua == False:
        try:
            valor = float(input('Insira aqui: '))
            if valor > 0:
                continua = True
            else:
                print('Valor Inválido')
        except ValueError:
            print('Digite apenas Números')
    return valor

def converter(real, dolar):
    valor = real / dolar
    return valor

print('Insira um valor em Reais na linha abaixo')
valor_em_reais = inserir()
print('Insira a atual cotação do dólar hoje [Quanto 1 Dólar vale em reais] na linha abaixo')
cotacao_dolar = inserir()
valor_em_dolares = converter(valor_em_reais, cotacao_dolar)
print(f'R${valor_em_reais} valem U${valor_em_dolares}')

# Exercício 2 ---------------------------------------------------------------

def inserir():
    continua = False
    while continua == False:
            try:
                valor = float(input('Insira aqui: '))
                if valor > 0:
                    continua = True
                else:
                    print('Valor Inválido')
            except ValueError:
                print('Digite apenas Números')
    return valor

def converter(real, dolar):
    valor = real / dolar
    return valor

def escolha():
    continua = False
    while continua == False:
        opcao = str(input('Deseja Continuar? [S/N]: ')).strip().upper()[0]
        if opcao not in 'SN':
            print('Opção Inválida')
        else:
            return opcao
    

print('='*30)
print('Conversor de Reais em Dólares')
print('='*30)
prossegue = True
while prossegue == True:
    
    print('Insira um valor em Reais na linha abaixo')
    valor_em_reais = inserir()
    print('Insira a atual cotação do dólar hoje [Quanto 1 Dólar vale em reais] na linha abaixo')
    cotacao_dolar = inserir()
    valor_em_dolares = converter(valor_em_reais, cotacao_dolar)
    print(f'R${valor_em_reais} valem U${valor_em_dolares}')
    
    opca = escolha()
    if opca == 'N':
        print('Finalizando...')
        prossegue = False
    else:
        print('Retornando...')

# Exercício 3 ---------------------------------------------------------------
def inserirminutos():
    continua = False
    while continua == False:
            try:
                print('Quanto tempo em minutos você esteve no estacionamento?')
                valor = float(input('Insira aqui: '))
                if valor > 0:
                    continua = True
                else:
                    print('Valor Inválido')
            except ValueError:
                print('Digite apenas Números')
    return valor

def veiculo():
    continua = False
    while continua == False:
        valor = str(input('Escolha entre CARRO OU MOTO: ')).strip().upper()
        match valor:
            case 'CARRO':
                continua = True
            case 'MOTO':
                continua = True
            case _:
                print('Digite corretamente, escolhendo entre CARRO OU MOTO')
    return valor

def calculo(veiculo, minutos):
    match veiculo:
        case 'CARRO':
            match minutos:
                case m if m <= 5:
                    preco = 0
                case m if m <= 60:
                    preco = 15
                case m if m >= 480:
                    preco = 50
                case _:
                    tempo_adicional = m - 60
                    preco = 15
                    while tempo_adicional > 0:
                        preco += 7.5
                        tempo_adicional -= 60
        case 'MOTO':
            match minutos:
                case m if m <= 5:
                    preco = 0
                case m if m <= 60:
                    preco = 10
                case m if m >= 480:
                    preco = 35
                case _:
                    tempo_adicional = m - 60
                    preco = 10
                    while tempo_adicional > 0:
                        preco += 5
                        tempo_adicional -= 60
    return preco

print('='*30)
print('ESTACIONAMENTO')
print('='*30)
meio = veiculo()
tempo = inserirminutos()
custo = calculo(meio, tempo)
print(f'O custo do estacionamento é de R${custo}')

# Exercício 4 ---------------------------------------------------------------

fibonacci = [0, 1]

def inseririnteiro():
    continua = False
    while continua == False:
            try:
                print('Quantos números você que que sejam mostrados')
                valor = int(input('Insira aqui: '))
                if valor > 0:
                    continua = True
                else:
                    print('Valor Inválido')
            except ValueError:
                print('Digite apenas Números Inteiros')
    return valor

algarismos = inseririnteiro()

for c in range (0, algarismos):
    if c >= 2:
        proximo = fibonacci[c-2] + fibonacci[c-1]
        fibonacci.insert(c, proximo)
    print(fibonacci[c], end=' ')

print('FIM')

# Exercício 5 ---------------------------------------------------------------

fibonacci = [0, 1]

def inseririnteiro():
    continua = False
    while continua == False:
            try:
                print('Quantos números você que que sejam mostrados')
                valor = int(input('Insira aqui: '))
                if valor > 0:
                    continua = True
                else:
                    print('Valor Inválido')
            except ValueError:
                print('Digite apenas Números Inteiros')
    return valor

algarismos = inseririnteiro()

for c in range (0, algarismos):
    if c >= 2:
        proximo = fibonacci[c-2] + fibonacci[c-1]
        fibonacci.insert(c, proximo)
        
for d in range(algarismos-1, -1, -1):
    print(fibonacci[d], end=' ')

print('FIM')