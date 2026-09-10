# Exercício 1
def escolabase():
    alunolist = []
    medialist = []
    cont = 1
    continua = True
    while continua == True:
        nome = str(input(f'Insira o nome do {cont}º aluno: '))
        prossegue = False
        while prossegue == False:
            media = float(input(f'Insira a média de {nome}: '))
            if media > 10 or media < 0:
                print('[INSIRA UMA NOTA VÁLIDA]')
            else:
                prossegue = True
        alunolist.append(nome)
        medialist.append(media)
        segue = False
        while segue == False:
            op = str(input('Deseja adicionar mais alunos? [S/N]: ')).upper().strip()[0]
            if op == 'S':
                cont += 1
                segue = True
            elif op == 'N':
                segue = True
                continua = False
            else:
                print('[INSIRA UMA OPÇÃO VÁLIDA]')
    for i in range(0, len(alunolist)):
        print(f'| ID: {i} | NOME: {alunolist[i]} | MÉDIA {medialist[i]} |')

# Exercício 2
def escolaadv():
    alunolist = []
    medialist = []
    cont = 1
    continua = True
    while continua == True:
        nome = str(input(f'Insira o nome do {cont}º aluno: '))
        prossegue = False
        while prossegue == False:
            media = float(input(f'Insira a média de {nome}: '))
            if media > 10 or media < 0:
                print('[INSIRA UMA NOTA VÁLIDA]')
            else:
                prossegue = True
        alunolist.append(nome)
        medialist.append(media)
        segue = False
        while segue == False:
            op = str(input('Deseja adicionar mais alunos? [S/N]: ')).upper().strip()[0]
            if op == 'S':
                cont += 1
                segue = True
            elif op == 'N':
                segue = True
                continua = False
            else:
                print('[INSIRA UMA OPÇÃO VÁLIDA]')
    search = str(input('Digite o nome do aluno que deseja pesquisar: '))
    encontrado = False
    for i in range(0, len(alunolist)):
        if search == alunolist[i]:
            idbuscador = i
            encontrado = True
    if encontrado == True:
        print(f'| ID: {idbuscador} | NOME: {alunolist[idbuscador]} | MÉDIA {medialist[idbuscador]} |')
    else:
        print(f'{search.upper()} NÃO ENCONTRADO')
        for i in range(0, len(alunolist)):
            print(f'| ID: {i} | NOME: {alunolist[i]} | MÉDIA {medialist[i]} |')

# Exercício 3
def gerencialist():
    nomes = [ "Ana", "Claudia", "Diego", "Diogo", "Elizia", "Fabricio", "Gabriella", "Marcelo", "Marcelly", "Tássia" ]
    medias = [ 8.5, 6.0, 4.5, 6.5, 9.5, 5.5, 8.0, 4.0, 9.0, 2.5]
    continua = True
    while continua == True:
        escolha = False
        while escolha == False:
            op = str(input("""O que deseja gerenciar?
[A] Alterar valor
[E] Excluir valor
[S] Sair do Gerenciador

Insira a opção que deseja: """)).upper().strip()[0]
            if op not in 'AES':
                print('Opção Inválida')
            else:
                escolha = True
        if op == 'A':
            confirmacao = False
            while confirmacao == False:
                index = int(input('Insira o número do index que deseja alterar (Começa em 0): '))
                novonome = str(input('Digite o novo nome: '))
                novomedia = float(input('Digite a nova média: '))
                opc = str(input('Confirma a alteração? [S/N]: ')).upper().strip()[0]
                if opc == 'S':
                    nomes[index] = novonome
                    medias[index] = novomedia
                    confirmacao = True
                else: 
                    print('Reiniciando alteração...')
        elif op == 'E':
            confirmacao = False
            while confirmacao == False:
                index = int(input('Insira o número do index que deseja deletar (Começa em 0): '))
                opc = str(input('Confirma a alteração? [S/N]: ')).upper().strip()[0]
                if opc == 'S':
                    nomes.pop(index)
                    medias.pop(index)
                    confirmacao = True
                else: 
                    print('Reiniciando alteração...')
        else:
            continua = False
    for i in range(0, len(nomes)):
            print(f'| ID: {i} | NOME: {nomes[i]} | MÉDIA {medias[i]} |')

# Index
while True:
    print("""Escolha qual exercício deseja acessar:
[1] Inserir alunos e médias e mostrar tudo no final
[2] Inserir alunos e médias e mostrar de um nome específico
[3] Gerenciar duas listas disponibilizadas para professor""")
    o = int(input('Digite a opção que deseja: '))
    if o == 1:
        escolabase()
    elif o == 2:
        escolaadv()
    else:
        if o == 3:
            gerencialist()
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
