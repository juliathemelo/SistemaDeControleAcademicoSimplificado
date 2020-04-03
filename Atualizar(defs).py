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
            if c.isnumeric() and len(codigod) < 4:
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



atualizardisciplina()


