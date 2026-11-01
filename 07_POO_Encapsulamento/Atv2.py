class cofre:
    def __init__(self,senha):
        self.__senha = senha
        self.__itens = []
        self.__aberto = False
        self.__tentativas = 0
        self.__bloqueado = False

    def abrir_cofre(self,senha_inserida):
        if self.__tentativas >= 3 and senha_inserida == self.__senha:
            print("Tentativas esgotadas, cofre está BLOQUEADO...")
            self.__bloqueado = True
        elif senha_inserida == self.__senha and self.__bloqueado == False:
            self.__aberto = True
            self.__tentativas = 0
            print("Cofre está aberto")
        self.__tentativas += 1
        print(f"Senha {senha_inserida} está errada, tentativa {self.__tentativas} de 3")
    def fechar_cofre(self):
        if self.__aberto:
            print("Fechando cofre...\nCofre está FECHADO agora")
            self.__aberto = False
    def inserir_item(self,item):
        if self.__aberto:
            self.__itens.append(item)
            print(f'O {item} foi inserido no cofre..')
        else:
            print("Abra o cofre primeiro!")
    def ver_itens(self):
        if self.__aberto:
            print(f'Itens : {self.__itens}')
        else:
            print("Abra o cofre primeiro!")

cofre1 = cofre(1225)
cofre2 = cofre(4939)

cofre1.inserir_item("goiaba")
cofre1.abrir_cofre(2251)
cofre1.abrir_cofre(1225)
cofre1.inserir_item("Colar de diamantes")
cofre1.ver_itens()
cofre1.fechar_cofre()

cofre2.abrir_cofre(1233)
cofre2.abrir_cofre(3909)
cofre2.abrir_cofre(4541)

