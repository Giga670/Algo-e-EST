Nome=(input("Digite seu nome: "))
Idade=(int(input("Digite sua idade: ")))
Turma=(input("Digite sua Turma: "))
if Idade<6:
    print("Idade insuficiente")
    Nome=0
    Idade=0
    Turma=0
else:
    print(f"Aluno {Nome} de {Idade} anos da turma do {Turma} ano cadastrado ")
