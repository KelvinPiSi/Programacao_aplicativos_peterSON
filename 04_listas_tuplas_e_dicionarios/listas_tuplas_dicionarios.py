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

# len() informa a quantidade de elementos
print(len(origin))

# Percorrendo uma lista
for nome in origin:
    print(nome)

# Verificando se um elemento existe
if "London" in origin:
    print("British Guy!")
else:
    print("Incorrect - loud buzz!")

# Lista com Diferentes tipos de dados
dados = ["Axl Low", 23, 1.79, True]
print(dados)

# Lista de números
notas = [7.5, 8, 6.5, 9]
soma = 0

for nota in notas:
    soma += nota

media = soma / len(notas)
print(f"Média: {media:.1f}")


# Tuplas
# Tuplas são semelhantes às listas
# A principal diferença é que tuplas não podem
# ser alteradas depois de criadas

coordenadas = (10,20)
print(coordenadas)

# Acessando os elementos
print(coordenadas[0])
print(coordenadas[1])


# Dicionários
# Armazena informações no formato:
# chave: valor

aluno = {
    "nome": "Kelvin",
    "idade": 17,
    "nota": 9.5
}

print(aluno)

# Acessando os valores
print(aluno["nome"])
print(aluno["idade"])
print(aluno["nota"])

# Alterando os valores

aluno["nota"] = 9
print(aluno)