class Product:
    def __init__(self,name,price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total = 0
    def subtotal(self):
        return self.price * self.quantity

class Cart:
    def __init__(self):
        self.item_list=[]

    def add(self,product):
        self.item_list.append(product)

    def total(self,total_purchase = 0):
        for produto in self.item_list:
            total_purchase += produto.subtotal()
        return total_purchase

    def show(self):
        # Exibe a lista de produtos com subtotal e o total geral
        print("=== Purchase extract ===")
        for produto in self.item_list:
            print(
                f"- {produto.name} (Qtd: {produto.quantity} | Un: R$ {produto.price:.2f}) -> Subtotal: R$ {produto.subtotal():.2f}"
            )
        print("-" * 40)
        print(f"Total Purchase: R$ {self.total():.2f}")

p1 = Product("Rice 5kg", 26.90, 2)
p2 = Product("Beans 1kg", 8.50, 3)
p3 = Product("Milk 1L", 4.80, 6)
p4 = Product("Coffe 500g", 15.30, 1)

TheCart = Cart()

TheCart.add(p1)
TheCart.add(p2)
TheCart.add(p3)
TheCart.add(p4)

TheCart.show()




