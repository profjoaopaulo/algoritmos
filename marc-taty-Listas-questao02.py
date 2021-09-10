lista = []

for i in range(10): #[0, 1, 2, ..., 9]
    x = float( input("Digite um valor real: ") )
    lista.append(x)

#lista[índice]

#for i in range(9, -1, -1): #[9, 8, 7, ..., 0]
#    print(lista[i], end = " ")

listaOriginal = lista.copy()

lista.reverse()

print(lista)
print(listaOriginal)