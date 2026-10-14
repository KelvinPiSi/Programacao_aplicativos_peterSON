class Cachorro:
    def __init__(self,nome, raca,idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        print(f"{self.nome} comentou: A situação economica atual do Brasil é uma de caso no qual se você não tirar vantagem do próximo, você irá ser passado para trás")
        print(f"{self.nome} Au Au!")
    def mostrar_dados(self):
        print(f"Nome -- {self.nome} -- Raça -- {self.raca} -- Idade -- {self.idade}")
    def correcao_dados(self):
        if self.idade < 8:
            self.idade += -1
            print(f"Nova idade é {self.idade}")
cachorro1 = Cachorro("Romeo", "Husky Siberiano", idade= 7)
cachorro2 = Cachorro("Delilah", "Pastor Alemão", idade= 4)

cachorro1.latir()
cachorro1.mostrar_dados()

cachorro2.latir()
cachorro2.mostrar_dados()

cachorro2.correcao_dados()

