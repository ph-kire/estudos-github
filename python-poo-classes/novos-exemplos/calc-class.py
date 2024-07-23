class Calculadora:
    def adicionar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Erro! Divisão por zero."

calc = Calculadora()
print("Adição:", calc.adicionar(5, 3))
print("Subtração:", calc.subtrair(5, 3))
print("Multiplicação:", calc.multiplicar(5, 3))
print("Divisão:", calc.dividir(5, 3))
