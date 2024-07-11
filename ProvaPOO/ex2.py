from random import randint

class Livro:
    pg_atual = 1
    def __init__(self, titulo, autor, qtd_paginas, guardado=True):
        self.titulo = titulo
        self.autor = autor
        self.qtd_paginas = qtd_paginas
        self.guardado = guardado
    
    def PegarLivro(self):
        if self.guardado == True:
            self.guardado = False
            print("O livro foi entregue")
        else:
            print("O livro não se encontra guardado no momento.")

    def DevolverLivro(self):
        if self.guardado == False:
            self.guardado = True
            print("O livro foi guardado")
        else:
            print("O livro se encontra guardado no momento.")

    def VirarUmaPagina(self):
        pg_atual = 0
        if self.guardado == False and pg_atual <= self.qtd_paginas:
            pg_atual = pg_atual + 1
            print(f"Página atual: {pg_atual}")
        else:
            print(f'Não dá para avançar páginas')

    def VirarNPaginas(self):
        n = randint(1,self.qtd_paginas)
        pg_atual = 0
        if self.guardado == False and pg_atual <= self.qtd_paginas:
            pg_atual = pg_atual + n
            print(f"Página atual: {pg_atual}")
        else:
            print(f'Não dá para avançar páginas')

    def VoltarUmaPagina(self):
        pg_atual = 2
        if self.guardado == False and pg_atual > 1 and pg_atual <= self.qtd_paginas:
            pg_atual = pg_atual - 1
            print(f"Página atual: {pg_atual}")
        else:
            print(f'Não dá para voltar páginas')
    
    def VoltarNPaginas(self):
        n = randint(1,self.qtd_paginas)
        pg_atual = 200
        if self.guardado == False and pg_atual > 1 and pg_atual <= self.qtd_paginas and n < pg_atual:
            pg_atual = pg_atual - n
            print(f"Página atual: {pg_atual}")
        else:
            print(f'Não dá para voltar páginas')

    def LerLivro(self):
        print(F'Autor: {self.autor}, Livro: {self.titulo}')

pl = Livro('oioi','abc',200)
pl.PegarLivro()
# pl.DevolverLivro()
# pl.VirarUmaPagina()
# pl.VirarNPaginas()
# pl.VoltarUmaPagina()
pl.VoltarNPaginas()
pl.LerLivro()
