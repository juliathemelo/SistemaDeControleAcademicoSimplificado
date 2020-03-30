def cadastroprofessor():
    arq = open("prof.txt","a")
    nome = input("Digite o nome do novo profesor(a): ")
    arq.write(nome)
    arq.write(" | ")
    dep = input("Digite o departamento do novo professor(a): ")
    arq.write(dep)
    arq.write(" | ")
    while True:
        cpf = input("Digite o CPF do novo professor(a)")
        if cpf.isnumeric() and len(cpf) == 11:
            arq.write(cpf)
            break
        else:
            print("CPF invalido")
    arq.write("\n")
    arq.close()

cadastroprofessor()
        
