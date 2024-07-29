
class Livro:
    def __init__(self, titulo, autor, ano, editora="Não informado"):

        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.editora = editora

    def exibir_info(self):
        print(f "{self.titulo}, {self.autor}, {self.ano}")
        