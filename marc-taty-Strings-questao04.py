#questão 04 - Strings
nome = input("Digite o seu nome: ")

for i in range(len(nome)):
    for j in range(i+1):
        print(nome[j], end="")
    
    print()


