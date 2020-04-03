#cadastros

def cadastroprofessor():
    arq = open("prof.txt","a")
    nome = input("Digite o nome do novo profesor(a): ")
    arq.write(nome)
    arq.write(" | ")
    dep = input("Digite o departamento do novo professor(a): ")
    arq.write(dep)
    arq.write(" | ")
    while True:
        cpf = input("Digite o CPF do novo professor(a): ")
        if cpf.isnumeric() and len(cpf) == 11:
            arq.write(cpf)
            break
        else:
            print("CPF invalido")
    arq.write("\n")
    arq.close()

def cadastroaluno():
    arq = open("aluno.txt","a")
    nome = input("Digite o nome do novo aluno(a): ")
    arq.write(nome)
    arq.write(" | ")
    curso = input("Digite o curso do novo aluno(a): ")
    arq.write(curso)
    arq.write(" | ")
    while True:
        cpf = input("Digite o cpf do novo aluno(a): ")
        if cpf.isnumeric and len(cpf) == 11:
            arq.write(cpf)
            break
        else:
            print("CPF invalido")
    arq.write("\n")
    arq.close

def cadastrodisciplina():
    arq = open("disciplina.txt","a")
    disciplina = input("Digite o nome da nova disciplina: ")
    arq.write(disciplina)
    arq.write(" | ")
    curso = input("Digite o curso onde vai adicionar a nova disciplina: ")
    arq.write(curso)
    arq.write(" | ")
    while True:
        codigo = input("Digite um código novo para a disciplina(4 números): ")
        if codigo.isnumeric and len(codigo)==4:
            arq.write(codigo)
            break
        else:
            ("Codigo Invalido")
    arq.write("\n")
    arq.close

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


#consultas

def consultaprofessor():
    arq = open("prof.txt","r")
    lista = arq.readlines()
    for i in lista:
        print(i)

def consultaaluno():
    arq = open("aluno.txt","r")
    lista = arq.readlines()
    for i in lista:
        print(i)

def consultadisciplina():
    arq = open("disciplina.txt","r")
    lista = arq.readlines()
    for i in lista:
        print(i)

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


#atualizar


def atualizarprofessor():
    arq = open('prof.txt', 'r')
    lista0 = arq.readlines()
    for x in lista0:
        print(x)
    
    arq.close()
    arq = open('prof.txt', 'r')
    dic = {}
    lista = arq.readlines()
    cpfprof = ''
    for i in lista:
        for c in i:
            if c.isnumeric() and len(cpfprof) < 11:
                cpfprof += c
        dic[i] = cpfprof
        cpfprof = ''
    arq.close()
    cpfinput = input('Digite aqui o CPF do professor que deseja atualizar: ')
    if cpfinput in dic.values():
        nome = input('Digite O Nome Atualizado: ')  
        cpf = input('Digite O CPF Atualizado: ')  
        departamento = input('Digite O Departamento Atualizado: ')
        arq = open('atual.txt', 'w')  
        arq.write('%s'%(nome))
        arq.write(' | ')
        arq.write('%s'%(departamento))
        arq.write(' | ')
        arq.write('%s'%(cpf))
        arq.write('\n')
        arq.close()
        arq = open('atual.txt', 'r')
        aux = arq.readlines()
        arq.close()
        for i in lista:
            if cpfinput == dic[i]:
                pos = lista.index(i)
                lista.pop(pos)
                lista.insert(pos, aux[0])
        arq = open('prof.txt', 'w')
        for i in lista:
            arq.write(i)
        arq.close()
    else:
        print('CPF INVALIDO.')
        

def atualizaraluno():
    arq = open('aluno.txt', 'r')
    lista0 = arq.readlines()
    for x in lista0:
        print(x)
    arq.close()

    arq = open('aluno.txt', 'r')
    dic = {}
    lista = arq.readlines()
    cpfaluno= ''
    for i in lista:
        for c in i:
            if c.isnumeric() and len(cpfaluno) < 11:
                cpfaluno += c
        dic[i] = cpfaluno
        cpfaluno = ''
    arq.close()
    cpfinput = input('Digite aqui o CPF do aluno que deseja atualizar: ')
    if cpfinput in dic.values():
        nome = input('Digite O Nome Atualizado: ')  
        cpf = input('Digite O CPF Atualizado: ')  
        curso = input('Digite O Curso Atualizado: ')
        arq = open('atual.txt', 'w')  
        arq.write('%s'%(nome))
        arq.write(' | ')
        arq.write('%s'%(curso))
        arq.write(' | ')
        arq.write('%s'%(cpf)) 
        arq.write('\n')
        arq.close()
        arq = open('atual.txt', 'r')
        aux = arq.readlines()
        arq.close()
        for i in lista:
            if cpfinput == dic[i]:
                pos = lista.index(i)
                lista.pop(pos)
                lista.insert(pos, aux[0])
        arq = open('aluno.txt', 'w')
        for i in lista:
            arq.write(i)
        arq.close()
    else:
        print('CPF INVALIDO.')


def atualizardisciplina():
    arq = open('disciplina.txt', 'r')
    lista0 = arq.readlines()
    for x in lista0:
        print(x)
    arq.close()

    arq = open('disciplina.txt', 'r')
    dic = {}
    lista = arq.readlines()
    codigod = ''
    for i in lista:
        for c in i:
            if c.isnumeric() and len(codigod)< 5 :
                codigod += c
        dic[i] = codigod
        codigod = ''
    arq.close()
    codinput = input('Digite aqui o Código da disciplina que deseja atualizar: ')
    if codinput in dic.values():
        nome = input('Digite O Nome Atualizado: ')  
        cod = input('Digite O Código Atualizado: ')  
        curso = input('Digite O Curso Atualizado: ')
        arq = open('atual.txt', 'w')  
        arq.write('%s'%(nome))
        arq.write(' | ')
        arq.write('%s'%(curso))
        arq.write(' | ')
        arq.write('%s'%(cod)) 
        arq.write('\n')
        arq.close()
        arq = open('atual.txt', 'r')
        aux = arq.readlines()
        arq.close()
        for i in lista:
            if codinput == dic[i]:
                pos = lista.index(i)
                lista.pop(pos)
                lista.insert(pos, aux[0])
        arq = open('disciplina.txt', 'w')
        for i in lista:
            arq.write(i)
        arq.close()
    else:
        print('CÓDIGO INVALIDO.')


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



#deletar


def deletarprofessor():
    arq = open('prof.txt', 'r')
    lista0 = arq.readlines()
    for x in lista0:
        print(x)
    arq.close()
    arq = open('prof.txt', 'r')
    dic = {}
    lista1 = arq.readlines()
    cpfprof = ''
    for i in lista1:
        for c in i:
            if c.isnumeric() and len(cpfprof) < 11:
                cpfprof += c
        dic[i] = cpfprof
        cpfprof = ''
    arq.close()
    cpfinput = input('CPF do professor que deseja deletar: ')
    if cpfinput in dic.values():
        for i in lista1:
            if cpfinput == dic[i]:
                pos = lista1.index(i)
                lista1.pop(pos)
        arq = open('prof.txt', 'w')
        for i in lista1:
            arq.write(i)
        arq.close()
    else:
        print('CPF Invalido.')


def deletaraluno():
    arq = open('aluno.txt', 'r')
    lista0 = arq.readlines()
    for x in lista0:
        print(x)
    arq.close()
    arq = open('aluno.txt', 'r')
    dic = {}
    lista1 = arq.readlines()
    cpf = ''
    for i in lista1:
        for c in i:
            if c.isnumeric() and len(cpf) < 11:
                cpf += c
        dic[i] = cpf
        cpf = ''
    arq.close()
    cpfinput = input('CPF do professor que deseja deletar: ')
    if cpfinput in dic.values():
        for i in lista1:
            if cpfinput == dic[i]:
                pos = lista1.index(i)
                lista1.pop(pos)
        arq = open('aluno.txt', 'w')
        for i in lista1:
            arq.write(i)
        arq.close()
    else:
        print('CPF Invalido.')


def deletardisciplina():
    arq = open('disciplina.txt', 'r')
    lista0 = arq.readlines()
    for x in lista0:
        print(x)
    arq.close()
    arq = open('disciplina.txt', 'r')
    dic = {}
    lista1 = arq.readlines()
    cod = ''
    for i in lista1:
        for c in i:
            if c.isnumeric() and len(cod) < 5:
                cod += c
        dic[i] = cod
        cod = ''
    arq.close()
    codinput = input('Codigo da disciplina que deseja deletar: ')
    if codinput in dic.values():
        for i in lista1:
            if codinput == dic[i]:
                pos = lista1.index(i)
                lista1.pop(pos)
        arq = open('disciplina.txt', 'w')
        for i in lista1:
            arq.write(i)
        arq.close()
    else:
        print('Codigo Invalido.')        



        



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



#layout do sistema

while True:
    print("Seja Bem-Vindo !")
    print("Acessos:\n 1 - Professor\n 2 - Alunos\n 3 - Disciplina\n 4 - Turmas\n 5 - Sair")
    acesso = (input("Digite a operação que deseja acessar:"))
    if acesso == "1":
        while True:
            print("Acessos:\n 1 -> Cadastrar Professor(a)\n 2 -> Atualizar Informação\n 3 -> Consultar Professor(a)\n 4 -> Deletar Professor(a)\n 5 -> Sair")
            prof = (input("Digite a operação que deseja realizar:"))
            if prof == "1":
                cadastroprofessor()
            elif prof == "2":
                atualizarprofessor()
            elif prof == "3":
                consultaprofessor()
            elif prof == "4":
                deletarprofessor()
            elif prof == "5":
                break


            
    if acesso == "2":
        while True:
            print("Acessos:\n 1 -> Cadastrar Aluno(a)\n 2 -> Atualizar Informação\n 3 -> Consultar Aluno(a)\n 4 -> Deletar Aluno(a)\n 5 -> Sair")
            aluno = (input("Digite a operação que deseja realizar:"))
            if aluno == "1":
                cadastroaluno()
            elif aluno == "2":
                atualizaraluno()
            elif aluno == "3":
                consultaaluno()
            elif aluno == "4":
                deletaraluno()
            elif aluno == "5":
                break



    if acesso == "3":
        while True:
            print("Acessos:\n 1 -> Cadastrar Disciplina\n 2 -> Atualizar Informação\n 3 -> Consultar Disciplina\n 4 -> Deletar Disciplina\n 5 -> Sair")
            disciplina = (input("Digite a operação que deseja realizar:"))
            if disciplina == "1":
                cadastrodisciplina()
            elif disciplina == "2":
                atualizardisciplina()
            elif disciplina == "3":
                consultadisciplina()
            elif disciplina == "4":
                deletardisciplina()
            elif disciplina == "5":
                break


    if acesso == "4":
        while True:
            print("Acessos:\n 1 -> Cadastrar Turma\n 2 -> Atualizar Informação\n 3 -> Consultar Turma\n 4 -> Deletar Turma\n 5 -> Sair")
            turma = (input("Digite a operação que deseja realizar:"))
            if turma == "1":
                cadastroturma()
            elif turma == "2":
                atualizarturma()
            elif turma == "3":
                consultarturma()
            elif turma == "4":
                deletarturma()
            elif turma == "5":
                break
            
    
