#------------------------------------------------------------------------
# Sistemas de Notas Versão 2.0
#------------------------------------------------------------------------
# Melhorias realizadas (Desafio Final):
# - Substituição das listas separadas por uma única "lista de dicionários"
# - Uso do módulo json nativo para salvar e carregar os dados
#------------------------------------------------------------------------

#------------------------------------------------------------------------
# Json
#------------------------------------------------------------------------

import json

lista_alunos = []

try:
    with open('notas.json', 'r') as arquivo:
        lista_alunos = json.load(arquivo)
except FileNotFoundError:
    lista_alunos = []

def salvar_dados():
    with open('notas.json', 'w') as arquivo:
        json.dump(lista_alunos, arquivo)

#------------------------------------------------------------------------
# Operadores Principais
#------------------------------------------------------------------------

def adicionar_nota(nome, nota):
    # Adicionando um item em um dicionário (dentro da lista)
    lista_alunos.append({"nome": nome, "media": nota})
    salvar_dados()

def alterar_nota(indice, nome, nota):
    # Alterando informações de um dicionário específico na lista
    lista_alunos[indice]["nome"] = nome
    lista_alunos[indice]["media"] = nota
    salvar_dados()

def listar_nota():
    # Percorrendo a estrutura com for
    for i in range(0, len(lista_alunos)):
        print(f'| ID: {i} | NOME: {lista_alunos[i]["nome"]} | MÉDIA {lista_alunos[i]["media"]} |')

def listar_nota_unica(i):
    print(f'| ID: {i} | NOME: {lista_alunos[i]["nome"]} | MÉDIA {lista_alunos[i]["media"]} |')

def excluir_nota(indice):
    # Utilizando a instrução del ensinada no Tópico 1 (item 12)
    del lista_alunos[indice]
    salvar_dados()

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

def solicitar_index(lista_alunos):
    valido = False
    while valido == False:
        try:
            index_aluno = int(input('Insira o Index do Aluno: '))
            if 0 <= index_aluno < len(lista_alunos):
                valido = True
            elif len(lista_alunos) == 0:
                print('Lista vazia')
                valido = True
                index_aluno = "ABORTAR"
            else:
                print(f"Index fora do intervalo! Digite um número entre 0 e {len(lista_alunos) - 1}.")      
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
            print("Alteração Confirmada")
        case 'N':
            print("Sem Alteração")
        case _:
            print('Digite corretamente')

def controller_listar_nota():
    listar_nota()

def controller_alterar_nota():
    continua = True
    while continua == True:
        index = solicitar_index(lista_alunos)
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
                    print("Alteração Confirmada")
                    continua = False
                case 'N':
                    print("Sem Alteração")
                case _:
                    print('Digite corretamente')

def controller_excluir_nota():
    continua = True
    while continua == True:
        index = solicitar_index(lista_alunos)
        if index == 'ABORTAR':
            print('Operação Cancelada')
            break
        else:
            opc = str(input("Confirma ? [S/N]: ")).upper().strip()[0]
            match opc:
                case 'S':
                    excluir_nota(index)
                    print("Alteração Confirmada")
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