class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.__nota = nota

    @property
    def nota(self):
        return self.__nota
    def definir_nota(self,nova_nota):
        if nova_nota < 0 and nova_nota >10:
            print("Nota inválida")
            return
        self.__nota = nova_nota

    def situacao(self):
        if self.nota < 7:
            return f"Aluno(a) {self.nome} está reprovado!"
        else:
            return f"Aluno(a) {self.nome} está aprovado!\n"f"Passou com nota de {self.nota}"


aluno1 = Aluno("Marina", 6.5)
aluno2 = Aluno("Pedro", nota=10)

print(aluno1.situacao())# Reprovado
aluno1.definir_nota(15)# Nota inválida!
aluno1.definir_nota(8)
print(aluno1.nota)# 8
print(aluno1.situacao())# Aprovado

print(aluno2.situacao())

try:
    aluno1.nota = 15
except AttributeError:
    print("Não é permitido alterar a nota  diretamente")

try:
    print(aluno2.__nota)
except AttributeError:
    print("O atributo __nota não pode ser acessado de fora")


