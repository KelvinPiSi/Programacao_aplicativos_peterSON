class Produto:

    def __init__(self,nome, preco,quantidade=0 ):
        self.nome = nome
        self.__preco = preco
        self.__quantidade = quantidade
    @property
    def preco(self):
        return self.__preco
    @property
    def quantidade(self):
        return self.__quantidade
    def entrada_qtd(self,estoque):
        if 0 < estoque :
            self.__quantidade += estoque
    def saida_qtd(self,estoque):
        if estoque <= self.quantidade:
            self.__quantidade -= estoque
        else:
            print(f'Estoque insuficiente para retirada\nEstoque no momento: {self.quantidade} Un')
    def desconto(self,porcentagem):
        if 1 <= porcentagem <= 50:
            self.__preco = self.preco* (porcentagem / 100)
        else:
            print("Desconto requerido incorreto, insira um valor entre 1 e 50 para obter seu desconto")
    def valor_estoque(self):
        print(f'Valor em estoque é: R${self.preco*self.quantidade}')



Boneca = Produto("Barbie ", 299.9, 100)
Carrinho = Produto("Hot wheels", 15.9)

Boneca.entrada_qtd(10)
Carrinho.entrada_qtd(5)

Boneca.saida_qtd(25)
Carrinho.saida_qtd(30)

Boneca.desconto(25)
Carrinho.desconto(64)

Boneca.valor_estoque()
Carrinho.valor_estoque()

try:
    Boneca.quantidade = 1000
except AttributeError as e:
    print(f"\nSucesso no teste de segurança: Alteração direta bloqueada ({e})")
