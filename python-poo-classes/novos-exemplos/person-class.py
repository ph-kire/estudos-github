class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

pessoa = Pessoa("Carlos", 35)
pessoa.cumprimentar()
