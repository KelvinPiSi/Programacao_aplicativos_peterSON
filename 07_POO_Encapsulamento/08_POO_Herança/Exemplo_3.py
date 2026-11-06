import sys
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
              f"Salário atual é R${self.__salario:.2f}")
    def bonus(self):
        return self.salario * 0.1

    @salario.setter
    def salario(self, value):
        self.__salario = value


pj1 = Funcionario("Ana", salario=3000)
pj2 = Funcionario("Gabriel", salario=2700)
pj3 = Funcionario("João", salario=3000)


pj1.apresentar()
print("Dia do Pagamento...")
print(pj1.salario)
pj1.ganho(2539)
pj1.apresentar()
print("Dia de Aumento")
pj1.aumento(-10)
pj1.aumento(20)

#Comandos de teste -→ try/except é um bloco usado para tratar erros

try:
    pj1.__salario = 1000000
except AttributeError:
    print("Não é permitido alterar o salário diretamente")

try:
    print(pj1.salario)
except AttributeError:
    print("O atributo __salario não pode ser acessado de fora")

# 2. Herança

class  Gerente(Funcionario):

        def __init__(self,nome,salario,equipe):
            super().__init__(nome,salario) # Chama o construtor da classe Mãe
            self.equipe = equipe
            self.integrantes = []
        def demissao(self,demissao):
            self.equipe =- demissao
        def mostrar_equipe (self,integrantes):
            self.integrantes.append(integrantes)
            print(f'{self.nome}gerencia indiretamente {self.equipe}')
            print(f'{self.nome} gerencia {self.integrantes}')

        def bonus(self):
            return self.salario * 0.20

Chefe1 = Gerente("Marcio", 12000.00, equipe=50)
Chefe1.mostrar_equipe(f"{pj1.nome,pj2.nome,pj3.nome}")

class Estagiario(Funcionario):
    def __init__(self, nome, salario,curso):
        super().__init__(nome,salario)
        self.curso = curso
    def pedir_demissao(self):
        print(f'{self.nome} pediu demissão')
        sys.exit()
    def bonus(self):
        return  200

estagiario1 = Estagiario("Thiago",1700, "Técnico em Internet")

Chefe1.aumento(30)

estagiario1.apresentar()

estagiario1.aumento(5)

# Polimorfismo

print("\nPolimorfismo\nExemplos de objetos reagindo diferentemente aos mesmos metodos")

grupo = [Funcionario("Gabriel", salario=2800),Gerente("João", salario=7500, equipe=6)
          ,Estagiario("Jonathan", salario=1600, curso="Modelagem de Sistemas")]

for funcionario in grupo:
    print(f"{funcionario.nome}: R$ {funcionario.bonus()}")

"""""
1. Criamos uma lista chamada equipe com funcionarios de classes diferentes,
2. Isso resultou em cada um dos objetos reagindo de maneira diferente ao mesmo método.
3. Usamos funcionario.bonus() e cada classs executou seu próprio cálculo.
"""""