class Alunos:
    nome = ''
    idade = 0
    turma = ''
    planta = ''

    def __init__(self, nome, idade, turma, planta):
        self._nome = nome
        self._idade = idade
        self._turma = turma
        self._planta = planta
    
    def getAlunos(self):
        return {'aluno': self._nome, 'idade': self._idade, 'turma': self._turma, 'planta': self._planta}

nome = input("Digite o nome do aluno(a): ")
idade = input("Digite o idade do aluno(a): ")
turma = input("Digite o turma do aluno(a): ")
planta = input("Digite o planta do aluno(a): ")

aluno = Alunos(nome, idade, turma, planta)
print(aluno.getAlunos())

# mariana = Alunos('Mariana',17,'DTA2','Curitiba')
# juliana = Alunos('Juliana',20,'DTA2','Curitiba')
# gabriel = Alunos('Gabriel',19,'TDS2','Campinas')
# helena = Alunos('Helena ',18,'DTA1','Curitiba')

# mariana.getAlunos()
# juliana.getAlunos()
# gabriel.getAlunos()
# helena.getAlunos()

aluno_str = str(aluno.getAlunos())
with open("alunos.txt","a", encoding="utf-8") as arquivo:
    arquivo.write(f'{aluno_str}\n')