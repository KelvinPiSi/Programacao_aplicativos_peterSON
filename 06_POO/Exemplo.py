#1. Classe: o modelo (planta)
import time


class Celular:
    def __init__(self, marca, modelo, cor, bateria = 100, ):
        #Atributos : caracteristícas do objeto
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria
        self.ligado = False

#4 Métodos: Comportamentos de um objeto

    def ligar(self):
            #Consulta um atributo do próprio objeto
            if self.bateria == 0:
                print("Celular está desligado! Coloque carregar")
            else:
                self.ligado = True
                self.bateria += -1
                print("Celular está ligado")
    def carregando(self):
        if self.bateria < 100:
            print("O celular está carregando...")
            time.sleep(10)
            self.bateria += 1
            print(f"Celular está em {self.bateria}%")
    def desligar(self):
        self.ligado = False
        print("Celular está desligado")
#5 Objetos : Criados a partir da classe
celular_1 = Celular("Beitong", "Garaxy", "Vermelho Amarelado", bateria = 95)
celular_2 = Celular("Motorola","Moto g69", "Azul pastel", bateria = 67)
#6 Acessando e alterando atributos

print(celular_1.marca)
print(celular_1.modelo)
print(celular_1.cor)
print(celular_1.bateria,"%")

#7 Chamando métodos
celular_1.ligar()
print(celular_1.bateria, "%")

celular_1.carregando()

celular_1.desligar()

