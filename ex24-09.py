# Exercício 1
def transforma():
    alunolist = []
    medialist = []

    def adicionar_nota(nome, nota):
        alunolist.append(nome)
        medialist.append(nota)

    def alterar_nota(indice, nome, nota):
        alunolist[indice] = nome
        medialist[indice] = nota

    def listar_nota():
        for i in range(0, len(alunolist)):
            print(f'| ID: {i} | NOME: {alunolist[i]} | MÉDIA {medialist[i]} |')
    
    def excluir_nota(indice):
        alunolist.pop(indice)
        medialist.pop(indice)

    adicionar_nota("João", 7.5)
    adicionar_nota("Maria Farah", 8.5)
    adicionar_nota("Henrique Lima", 7)
    adicionar_nota("Claudio José", 5.5)
    listar_nota()
    nada = str(input("Aperte ENTER para continuar: "))

    alterar_nota(0, "João Silva", 6.5)
    listar_nota()
    nada = str(input("Aperte ENTER para continuar: "))

    excluir_nota(2)
    listar_nota()
    nada = str(input("Aperte ENTER para continuar: "))

# Exercício 2
def transformatch_case():
    alunolist = []
    medialist = []

    def adicionar_nota(nome, nota):
        alunolist.append(nome)
        medialist.append(nota)

    def alterar_nota(indice, nome, nota):
        alunolist[indice] = nome
        medialist[indice] = nota

    def listar_nota():
        for i in range(0, len(alunolist)):
            print(f'| ID: {i} | NOME: {alunolist[i]} | MÉDIA {medialist[i]} |')
    
    def excluir_nota(indice):
        alunolist.pop(indice)
        medialist.pop(indice)

    continua = True
    while continua == True:
        print("""Escolha qual opção deseja acessar:
[1] Adicionar Nota
[2] Consultar Nota
[3] Alterar Nota
[4] Excluir Nota
[0] Sair""")
        op = int(input("Digite a opção que deseja: "))
        match op:
            case 1:
                adicionar_nota("João", 7.5)
                adicionar_nota("Maria Farah", 8.5)
                adicionar_nota("Henrique Lima", 7)
                adicionar_nota("Claudio José", 5.5)
            case 2:
                listar_nota()
            case 3:
                alterar_nota(0, "João Silva", 6.5)
            case 4:
                excluir_nota(2)
            case 0:
                continua = False
            case _:
                    print('Digite corretamente')     

# Index
while True:
    print("""Escolha qual exercício deseja acessar:
[1] Tranformar ações dos programas anteriores de notas em funções
[2] Exercício anterior aplicando Match-Case
[3] Placeholder""")
    o = int(input('Digite a opção que deseja: '))
    match o:
        case 1:
            transforma()
        case 2:
            transformatch_case()
        case 3:
            print("placeholder")
        case _:
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