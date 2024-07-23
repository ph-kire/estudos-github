class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

retangulo = Retangulo(5, 10)
print("Área:", retangulo.area())
print("Perímetro:", retangulo.perimetro())
