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

        
