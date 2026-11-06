class Product:
    def __init__(self,name, price, stock=0):
        self.name = name
        self.price = price
        self.__stock = stock

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, value):
        self.__stock = value

    def refill(self,quantity):
        if quantity > 0:
            self.__stock += quantity
            print(f"{quantity} Un was added to the stock\nNew stock is {self.stock}")
        else:
            print("The quantity asked to be refilled is invalid")
    def sell(self,quantity):
        if quantity > 0 < self.stock:
            self.__stock -= quantity
            print(f"{quantity} Un was sold from stock\nNew stock is {self.stock}")
        else: print("There's no units left in stock to be sold")

    def informations(self):
        print(f"Name - {self.name}\nPrice - {self.price:2f}\nIn stock - {self.stock}")

    def final_price(self,taxes=10):
        return self.price * (1 + taxes/100)
    def total_price_in_stock(self):
        print(f"Total price in stock is: R${self.price * self.stock}")
print("\n---Part 1---\n")
obj1 = Product("object", price=20, stock=5)
obj1.refill(15)
obj1.sell(20)
obj1.refill(-50)
obj1.sell(25)
obj1.informations()
print(obj1.final_price())

try:
    obj1.stock = 1000000
except AttributeError:
    print("Can't change the stock quantity  directly")

class Eletronic(Product):
    def __init__(self,name, price, stock,guarantee=0):
        super().__init__(name, price, stock)
        self.guarantee = guarantee

    def final_price(self, taxes=20):
        self.guarantee += 5
        return self.price * (1 + taxes / 100) + self.guarantee

class Food(Product):
    def __init__(self,name,expiration_date, price, stock):
        super().__init__(name, price, stock)
        self.expiration_date = expiration_date

    def final_price(self, taxes=5):
        return self.price * (1 + taxes / 100)

    def show_expiriation(self):
        print(f'Product is going to expire on {self.expiration_date}')
print("\n---Part 2---\n")
obj2 = Food("Orange", "2026-07-20", price=1.89, stock=530)


if isinstance(obj2, Product):
    print(f"{obj2.name} is an Product\n")

print("\n---Part 3---\n")
Cart =[Food("Banana Silver","2026-07-27",price=1.99,stock=650),
       Eletronic("Notebook Positivo", price=2999.99,stock=20),Food("Apple Fuji","2026-07-23",price=1.50,stock=540),
       Eletronic("ESP32", price=299.99, stock=24)]
for Product in Cart:
    print(f"Name - {Product.name}\nPrice - {Product.price}")

print("\n---Extra Challenge ---\n")
print("Showing total price currently in stock")
obj2.informations()
obj2.total_price_in_stock()


