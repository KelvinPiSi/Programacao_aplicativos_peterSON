class Character:
    def __init__(self, name, role,):
        self.name = name
        self.role = role
        self.hp = 100
        self.lv = 1

    def damage_taken(self,dmg):
        self.hp = self.hp - dmg
        print(f'{self.name} has taken {dmg} damage!')
        if self.hp == 0 or self.hp < 0:
            print(f'{self.name} has been defeated!')
        elif self.hp < 20 :
            print(f'{self.name} is in critical condition!')
    def heal(self, healing):
        self.hp += healing
        print(f'{self.name} used healing, {healing} restored!')
        if self.hp > 100:
            self.hp = 100
    def levelling(self,level_up):
        self.lv =+ level_up
        self.hp = 100
    def status(self):
        print(f'Name -- {self.name}\nRole -- {self.role}\nLevel -- {self.lv}\nHp -- {self.hp}')
Player1 = Character("Aragon", "Arcanist")
Player2 = Character("Ivan Kortsch", "Fighter")

print("Mankind knew that they couldn't change society...\nSo instead of reflecting on themselves, they blamed the beasts\nHeaven or Hell")
Player1.status()
Player2.status()
print("Round one")
Player1.damage_taken(35)
Player2.damage_taken(55)
print("Round two")
Player1.heal(20)
Player2.damage_taken(25)
print('Round three')
Player1.damage_taken(60)
Player2.levelling(1)
print('Round four')
Player2.heal(25)
Player1.damage_taken(55)
print("Battle's over")

