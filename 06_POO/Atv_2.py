class Livro:

    def __init__(self, titulo, autor, total_paginas):
        self.titulo = titulo
        self.autor = autor
        self.total_paginas = total_paginas
        self.paginas_lidas = 0

    def ler(self, paginas):
        self.paginas_lidas += paginas
        print(f'{paginas} páginas foram lidas')
        if self.paginas_lidas > self.total_paginas:
            self.paginas_lidas = self.total_paginas

    def porcentagem_lida(self):
        if self.total_paginas == 0:
            return 0.0
        return (self.paginas_lidas / self.total_paginas) * 100

    def paginas_restantes(self):
        return self.total_paginas - self.paginas_lidas

    def terminou(self):
        return self.paginas_lidas == self.total_paginas



livro1 = Livro("Dm Quixote", "Miguel de Cervantes", 989)
livro2 = Livro("O Hobbit", "J.R.R. Tolkien", 310)

print(f"=== {livro1.titulo} ===")
livro1.ler(135)
print(f"Porcentagem lida: {livro1.porcentagem_lida()}%")
print(f"Páginas restantes: {livro1.paginas_restantes()}")
print(f"Terminou? {livro1.terminou()}\n")

livro1.ler(900)
print(f"Porcentagem lida: {livro1.porcentagem_lida()}%")
print(f"Páginas restantes: {livro1.paginas_restantes()}")
print(f"Terminou? {livro1.terminou()}\n")

print(f"=== {livro2.titulo} ===")
livro2.ler(150)
print(f"Porcentagem lida: {livro2.porcentagem_lida()}%")
print(f"Páginas restantes: {livro2.paginas_restantes()}")
print(f"Terminou? {livro2.terminou()}\n")

livro2.ler(160)
print(f"Porcentagem lida: {livro2.porcentagem_lida()}%")
print(f"Páginas restantes: {livro2.paginas_restantes()}")
print(f"Terminou? {livro2.terminou()}")




