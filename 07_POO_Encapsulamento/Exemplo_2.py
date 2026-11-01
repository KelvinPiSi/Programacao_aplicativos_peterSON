#1. Encapsulamento -≥ Proteger 0 salário para que só mude seguindo regras(métodos)
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario  # "__" == Privado || "_" == Protegido

    def apresentar(self):
        print(f"Nome -- {self.nome}\nSalario -- {self.salario}")

    @property
    def salario(self):
        return self.__salario

    def ganho(self, extrato):
        self.__salario += extrato

    def aumento(self,porcentagem):
        if porcentagem <= 0:
            print(f"Aumento inválido para {self.nome}")
            return
        self.__salario = self.__salario * (1 + porcentagem/100)
        print(f"{self.nome} recebeu {porcentagem}% de aumento.\n"
              f"Salário atual é R${self.__salario}")


pj1 = Funcionario("Ana", salario=3000)
pj1.apresentar()
print("Dia do Pagamento...")
print(pj1.salario)
pj1.ganho(2539)
pj1.apresentar()
print("Dia de Aumento")
pj1.aumento(-10)
pj1.aumento(20)

#Comandos de teste --> try/except é um bloco usado para tratar erros

try:
    pj1.salario = 1000000
except AttributeError:
    print("Não é permitido alterar o salário diretamente")

try:
    print(pj1.__salario)
except AttributeError:
    print("O atributo __salario não pode ser acessado de fora")