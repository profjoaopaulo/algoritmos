nome = input("nome: ")

nome2 = nome.upper() #convertido para maiúsculo

print(nome2[::-1])

'''
t = len(nome2)

nome2_inverso = []

for i in range(t - 1, -1, -1):
    nome2_inverso.append( nome2[i] )
    print(nome2_inverso[ t - i -1 ], end = "")

print()
'''
