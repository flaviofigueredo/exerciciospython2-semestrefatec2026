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

def listar_nota_unica(i):
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
            nome = str(input("Digite seu nome: ") )
            nota = float(input("Digite sua nota: ") )
            opc = str(input("Confirma ? [S/N]: ")).upper().strip()[0]
            match opc:
                case 'S':
                    adicionar_nota(nome, nota)
                    listar_nota_unica(index)
                    print("Alterção Confirmada")
                case 'N':
                    print("Sem Alteração")
                case _:
                    print('Digite corretamente')
        case 2:
            listar_nota()
        case 3:
            index = (int(input("Digite o index do aluno que deseja alterar")))
            nome = str(input("Digite seu nome: ") )
            nota = float(input("Digite sua nota: ") )
            opc = str(input("Confirma ? [S/N]: ")).upper().strip()[0]
            match opc:
                case 'S':
                    alterar_nota(index, nome, nota)
                    listar_nota_unica(index)
                    print("Alterção Confirmada")
                case 'N':
                    print("Sem Alteração")
                case _:
                    print('Digite corretamente')
        case 4:
            index = (int(input("Digite o index do aluno que deseja excluir")))
            opc = str(input("Confirma ? [S/N]: ")).upper().strip()[0]
            match opc:
                case 'S':
                    excluir_nota(index)
                    print("Alterção Confirmada")
                case 'N':
                    print("Sem Alteração")
                case _:
                    print('Digite corretamente')
        case 0:
            continua = False
        case _:
                print('Digite corretamente')