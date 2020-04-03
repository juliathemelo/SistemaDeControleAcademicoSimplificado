def cadastroturma():
    codigot = input("Digite aqui o codigo da nova turma(4 digitos): ")
    arq = open("turmas/%s.txt"%(codigot),"a")
    arq.write("Codigo da turma: %s"%(codigot))
    arq.write(" | ")
    periodo = input("Periodo da nova turma: ")
    arq.write("Periodo: %s"%(periodo))
    arq.write(" | ")
    codigod = input("Codigo da Disciplina: ")
    arq.write("Codigo da Disciplina: %s"%(codigod))
    arq.write("\n")
    quantidadep = int(input("Digite quantos professores deseja adicionar para a nova turma: "))
    listap = []
    listaa = []
    for i in range(quantidadep):
        while True:
            cpf = input("Digite o cpf deste professor: ")
            if cpf.isnumeric and len(cpf)==11:
                arq.write("Professor: ")
                arq.write(cpf)
                listap.append(cpf)
                arq.write("\n")
                arq.close
                break
            else:
                print("CPF Invalido")
    quantidadea = int(input("Digite quantos alunos deseja adicionar para a nova turma: "))
    for i in range(quantidadea):
        while True:
            cpf = input("Digite o cpf deste aluno: ")
            if cpf.isnumeric and len(cpf)==11:
                arq = open("turmas/%s.txt"%(codigot),"a")
                arq.write("Aluno: ")
                arq.write(cpf)
                listaa.append(cpf)
                arq.write("\n")
                arq.close
                break
            else:
                print("CPF Invalido")
    arq = open('turmas/%s.txt'%(codigot),'a')
    arq.write('\n')
    arq.write('Turma:%s '%(codigot))
    arq.close()

def consultarturma():
    codigot = input("Digite o codigo da turma que deseja consultar: ")
    arq = open('turmas/%s.txt'%(codigot), 'r')  
    lista = arq.readlines()
    for i in lista:
        if lista.index(i) == 0:
            print(i)
        else:
            print('-', i)
        arq.close()

def atualizarturma():
    codigot = input('Digite o codigo da turma que deseja atualizar:')
    y = 1
    arq = open('turmas/%s.txt'%(codigot),'r')
    lista = arq.readlines()
    for i in lista:
        print(y,"-",i)
        y += 1
    arq.close()
    arq = open('atual.txt','w')
    while True:
        print("Selecione a seguir o que deseja atualizar")
        print('1= Professor \n2= Aluno\n3= Periodo e Codigo da Disciplina e Turma')
        atual = input('O que deseja atualizar(colocar o digito da frente): ')
        if atual == '1':
            a = int(input('Digite a posição que deseja atualizar:'))
            while True:
                cpfp = input('CPF do professor:')
                if cpfp.isnumeric() and len(cpfp) == 11:
                    arq.write('Professor: %s'%(cpfp))
                    break
                else:
                    print('CPF NAO VALIDO')
            arq.write('\n')
            break
        elif atual == '2':
            a = int(input('Digite a posição que deseja atualizar:'))
            while True:
                cpfa = input('CPF do aluno:')
                if cpfa.isnumeric() and len(cpfa) == 11:
                    arq.write('Aluno: %s'%(cpfa))
                    break
                else:
                    print('CPF NAO VALIDO')
            arq.write('\n')
            break
        elif atual == '3':
            a = int(input('Digite a posição que deseja atualizar:'))
            codigot = input('Codigo da Turma:')
            arq.write('Codigo da Turma: %s'%(codigot))
            arq.write(' | ')
            peri = (input('Periodo:'))
            arq.write('Periodo: %s'%(peri))
            arq.write(' | ')
            codigod = (input('Codigo da Disciplina:'))
            arq.write('Codigo da Disciplina: %s'%(codigod))
            arq.write('\n')
            break
        else:
            print('Operação Invalida')
        arq.close()
    arq = open('atual.txt','r')
    auxl = arq.readlines()
    arq.close()
    arq = open('turmas/%s.txt'%(codigot),'w')
    lista.pop(a-1)
    lista.insert(a-1,auxl[0])
    for i in lista:
        arq.write(i)
    arq.close()
    arq = open('turmas/%s.txt'%(codigot),'r')
    lista = arq.readlines()
    for i in lista:
        print(i)
    arq.close()


def deletarturma():
    codigot = input("Digite o codigo da turma que deseja deletar algo: ")
    arq = open("turmas/%s.txt"%(codigot))
    y = 0
    lista = arq.readlines()
    for i in lista:
        if lista.index(i) == 0:
            print(i)
        else:
            print(y,"-",i)
        y += 1
    arq.close()
    if len(lista) > 1:
        a = int(input('Insira a posicao da turma que voce deseja deletar: '))
        b = input('Insira o codigo da turma novamente para confirmar o delete: ')
        arq = open('turmas/%s.txt'%(b), 'w')
        lista.pop(a)
        for i in lista:
            arq.write(i)
        arq.close()
        arq = open('turmas/%s.txt'%(b), 'r')
        y = 0
        lista = arq.readlines()
        print(''*80)
        print('Elemento deletada com sucesso, confira com a nova lista abaixo:')
        for i in lista:
            if lista.index(i) == 0:
                print(i)
            else:
                print(y, '-', i)
            y += 1
        arq.close()
    else:
        print('_' * 80)
        print('\nNenhuma turma encontrada.')
    


def ata():

