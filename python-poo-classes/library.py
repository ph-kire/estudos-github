class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def adicionar_livro(self, livro):
        self.catalogo.append(livro)
        print(f"Livro '{livro.titulo}' adicionado ao catálogo.")

    def listar_livros(self):
        if len(self.catalogo) == 0:
            print("O catálogo está vazio.")
        else:
            for livro in self.catalogo:
                print(f"Título: {livro.titulo}, Autor: {livro.autor}")

livro1 = Livro("1984", "George Orwell")
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.listar_livros()
