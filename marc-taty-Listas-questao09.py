#Questão 09 (Listas)
vetor = []
soma = 0

for i in range(10):
    vetor.append( int( input("Digite um inteiro: ") ) )
    vetor[i] **= 2 #faz o quadrado do valor lido
    soma += vetor[i]

print(vetor)
print("Soma =", soma)


#vetor = [1, 4, ..., 100]
#índices  0  1  ...  9

















