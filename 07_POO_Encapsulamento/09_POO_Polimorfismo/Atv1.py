from time import sleep


class Character:
    def __init__(self, name,hp=100):
        self.name = name
        self.__hp = hp

    def take_damage(self,dmg):
        if dmg >= 0 < self.__hp:
            self.__hp -= dmg
            print(f"{self.name} has taken {dmg} damage!")
            if self.__hp < 0:
                self.__hp = 0
        else:
            print("Invalid damage value")
    def healing(self,heal):
        if heal >= 0 < self.__hp:
            self.__hp += heal
            print(f"{self.name} has recovered {heal} hp!")
            if self.__hp > 100:
                self.__hp = 100
        else:
            print("Invalid heal value")
    def status(self):
        print(f"Name - {self.name}\nHP - {self.__hp}")
    def attack(self,attack=10):
        print(f"{self.name} has an attack of {attack}")

class Warrior(Character):
    def __init__(self, name,hp=100, strenght=15):
        super().__init__(name,hp)
        self.strenght = strenght

    def attack(self,attack=10):
            return self.strenght + attack

class Mage(Character):
    def __init__(self, name,hp=100, mana=50):
        super().__init__(name,hp)
        self.mana = mana
    def status_mana(self):
        print(f"Mana - {self.mana}")

    def attack(self, attack = 25,cost=10):
        self.mana -= cost
        if self.mana < cost:
            return 5
        else:
            return attack

class Boss(Character):
    def __init__(self, name,hp=1000):
        super().__init__(name,hp)

print("\n---Part 1---\n")
Chara1 = Character("Ixian")
Chara2 = Character("Deepian")

Chara1.status()
Chara2.take_damage(20)

Chara1.take_damage(80)

Chara1.healing(150)
Chara1.status()

Chara2.attack()

Chara1.take_damage(-10)


try:
    Chara1.hp = 1000000
except AttributeError:
    print("Can't change the hp value directly")

print("\n---Part 2---\n")
chara3 = Warrior("Lash")
chara4 = Mage("Celeste")
chara3.status()
chara4.status()
chara4.status_mana()

chara3.attack()
chara4.healing(50)
chara3.take_damage(70)

if isinstance(chara4, Character):
     print("\nThe mage is a character")

print("\n---Part 3---\n")

hero_party = [Warrior("Eisen",strenght=100),Mage("Frieren", mana=5000), Warrior("Himmel", strenght=50),
              Mage("Heiter", mana=2500)]

for Character in hero_party:
    print(f"{Character.name} has an attack of {Character.attack()}")

print("\n--- Extra---\n")

BBG = Boss("Zoltraak", hp=1500)

print("An foe is approaching rapidly...")
sleep(3)
print(f"{BBG.name} has awoken!")

BBG.status()





