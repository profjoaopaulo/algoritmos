#questão 01 (Funções)

n = int(input("Digite um inteiro: "))

#Definição da função
def piramideNumerica(numero):
    for i in range(numero): #roda pelas linhas
        for j in range(i+1):
            print(i+1, end = "  ")
        print()

piramideNumerica(n)
