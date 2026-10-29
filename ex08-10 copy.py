#------------------------------------------------------------------------
# Sistemas de Notas Versão 1.0
#------------------------------------------------------------------------
# Melhorias realizadas:
# - Implementação e Separação do código entre Index, Controller e Operador
#------------------------------------------------------------------------

# Operadores Principais

#------------------------------------------------------------------------
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
#------------------------------------------------------------------------

# Operadores Auxiliares

#------------------------------------------------------------------------

def solicitar_nome():
    nome_aluno = ""
    while len(nome_aluno) == 0:
        nome_aluno = str(input('Insira o Nome do Aluno: '))
    return nome_aluno

def solicitar_media():
    valido = False
    while valido == False:
        media_aluno = str(input('Insira a Média do Aluno: '))
        try:
            numero = float(media_aluno)
            valido = True
        except ValueError:
            print("Valor inválido! Por favor, digite apenas números.")
    return numero

def solicitar_index(alunolist):
    valido = False
    while valido == False:
        try:
            index_aluno = int(input('Insira o Index do Aluno: '))
            if 0 <= index_aluno < len(alunolist):
                valido = True
            elif len(alunolist) == 0:
                print('Lista vazia')
                valido = True
                index_aluno = "ABORTAR"
            else:
                print(f"Index fora do intervalo! Digite um número entre 0 e {len(alunolist) - 1}.")      
        except ValueError:
            print("Valor inválido! Por favor, digite apenas números inteiros.")
    return index_aluno
#------------------------------------------------------------------------

# Controladores

#------------------------------------------------------------------------
def controller_adicionar_nota():
    nome = solicitar_nome()
    nota = solicitar_media()
    opc = str(input("Confirma ? [S/N]: ")).upper().strip()[0]
    match opc:
        case 'S':
            adicionar_nota(nome, nota)
            print("Alterção Confirmada")
        case 'N':
            print("Sem Alteração")
        case _:
            print('Digite corretamente')

def controller_listar_nota():
    listar_nota()

def controller_alterar_nota():
    continua = True
    while continua == True:
        index = solicitar_index(alunolist)
        if index == 'ABORTAR':
            print('Operação Cancelada')
            break
        else:
            nome = solicitar_nome()
            nota = solicitar_media()
            opc = str(input("Confirma ? [S/N]: ")).upper().strip()[0]
            match opc:
                case 'S':
                    alterar_nota(index, nome, nota)
                    listar_nota_unica(index)
                    print("Alterção Confirmada")
                    continua = False
                case 'N':
                    print("Sem Alteração")
                case _:
                    print('Digite corretamente')

def controller_excluir_nota():
    continua = True
    while continua == True:
        index = solicitar_index(alunolist)
        if index == 'ABORTAR':
            print('Operação Cancelada')
            break
        else:
            opc = str(input("Confirma ? [S/N]: ")).upper().strip()[0]
            match opc:
                case 'S':
                    excluir_nota(index)
                    print("Alterção Confirmada")
                    continua = False
                case 'N':
                    print("Sem Alteração")
                case _:
                    print('Digite corretamente')
#------------------------------------------------------------------------

# Index

#------------------------------------------------------------------------
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
            controller_adicionar_nota()
        case 2:
            controller_listar_nota()
        case 3:
            controller_alterar_nota()
        case 4:
            controller_excluir_nota()
        case 0:
            continua = False
        case _:
                print('Digite corretamente')
#------------------------------------------------------------------------