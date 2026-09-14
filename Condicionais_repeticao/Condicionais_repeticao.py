codigo = int(input("Insira o código do livro: "))
nome = ("Weg Tintas")

if( codigo >= 120900):
    print(f"Esse livro pertence à {nome}\n\n")

elif(codigo <= 120900):
    print("Este livro pertence à Weg 2\n\n")
else:
    print("Este livro não pertence a nenhuma instalação Weg\n\n")

# utilizando #and/#or/#not para valores lógicos

livro = "A biografia de um Amazonense"

data_publicacao = 2020

emprestavel = True

if data_publicacao >= 2012 and emprestavel:
    print(f"Livro {livro} disponível para empréstimo")
else:
    print(f"Livro {livro} não disponível para empréstimo")


## While, AGAIN(ST)
i = 0
timer = 1

while timer <= 6:
        print(timer)
        timer += 1

#We're in FOR hell

for  numero in range(10, 0, -1):
    print(numero)

#Welcome to the Listground...
#how was the fall?


print("Facções da Sala :")
nomes = ["Tramontina", "Os Primos", "Kaue e os skanks", "Big Mafia", "Kurtztistas"]

for nome in reversed(nomes):
    print(nome)

## I'm gonna give ya a Break, then Continue and maybe Pass

for numero in range(1,11):
    print("Break")
    if numero == 6:
        numero += 1
        break

    print("Continue")
    print(numero)
    if numero == 6:
        numero += 1
        continue

    print("Pass")
    print(numero)
    if numero == 6:
        numero += 1
        pass
    print(numero)


