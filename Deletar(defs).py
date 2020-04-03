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



deletaraluno()
    
