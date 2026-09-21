#Arra... Listas, t(d)uplas e dicionarios
#Lista = Essencialmente uma array, são mutáveis

origin = ["United Kingdom", "London", "St.Maria avenue"]

#É possível acessar o último elemento com -1 no print

print(f"Origin : {origin[-1]}")

# É possivel alterar um elemento de uma lista

origin[0] = "New earth"
print(origin[0])

origin[1] = "Illyria"

#Também é possível adicionar elementos a uma lista

origin.append("The Backyard")

print(origin[3])

#append e insert diferem na questão da ordem de adição do elemento

origin.insert(2,"The Future")

print(origin[2])
#Remove é como o proprio comando descreve, remove um valor

origin.remove("St.Maria avenue")
#Pop remove pelo indice um elemento

origin.pop(2)

print(origin)

#Tuplas = é uma lista constante, sendo imutáveis. O nome é horrível

my_time = ("frozen still", "no change", "café made him hungry")

print(f"His time was : {my_time[0]}")

#Dicionário = "Alexa, qual o significado da palavra ..."

Axl_Low = {"nome": "Axl Low", "idade ": 23}

print(f"He was : {Axl_Low["nome"]}")