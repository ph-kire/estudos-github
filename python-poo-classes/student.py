class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)


aluno = Aluno("Maria")
aluno.adicionar_nota(8)
aluno.adicionar_nota(9)
aluno.adicionar_nota(7)
print(f"Média das notas de {aluno.nome}: {aluno.calcular_media()}")
