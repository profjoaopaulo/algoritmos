#questão 07 - Strings
frase = input("Digite uma frase: ")

numEspaco = frase.count(" ")
numVogais = []
vogais = ['a', 'e', 'i', 'o', 'u'] #atualizar a questão para contar também vogais 
                                   #Maiúsculas ['A', 'E', 'I', 'O', 'U']

for i in range(5):
    numVogais.append(frase.count(vogais[i]))

print("Na frase tem", numEspaco, "espaços em branco!")

somaVogais = 0
for i in range(5):
    print("Possui o caractere", vogais[i], numVogais[i], "vezes!")
    somaVogais += numVogais[i]

print("Portanto, são", somaVogais, "vogais ao todo!")





