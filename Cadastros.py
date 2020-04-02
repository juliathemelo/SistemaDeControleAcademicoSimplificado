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


    
cadastroaluno()

