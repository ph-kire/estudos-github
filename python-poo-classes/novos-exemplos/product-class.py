class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade
        print(f"{quantidade} unidades adicionadas. Estoque atual: {self.quantidade}")

    def remover_estoque(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
            print(f"{quantidade} unidades removidas. Estoque atual: {self.quantidade}")
        else:
            print("Quantidade insuficiente em estoque.")

    def informacoes(self):
        print(f"Produto: {self.nome}, Preço: {self.preco}, Quantidade em estoque: {self.quantidade}")

produto = Produto("Notebook", 1500.00, 10)
produto.informacoes()
produto.adicionar_estoque(5)
produto.remover_estoque(3)
