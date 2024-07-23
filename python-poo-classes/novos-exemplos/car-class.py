class Carro:
    def __init__(self, marca, modelo, ano, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"O carro acelerou para {self.velocidade} km/h.")

    def frear(self, decremento):
        if self.velocidade - decremento >= 0:
            self.velocidade -= decremento
            print(f"O carro desacelerou para {self.velocidade} km/h.")
        else:
            self.velocidade = 0
            print("O carro parou.")

    def informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Velocidade: {self.velocidade} km/h")

carro = Carro("Toyota", "Corolla", 2020)
carro.informacoes()
carro.acelerar(30)
carro.frear(10)
