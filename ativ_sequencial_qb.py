#Questão B da Atividade de Estrutura Sequencial
a1 = float( input("A1: ") )
r = float( input("R: ") )
n = int( input("N: ") ) #posição do termo a ser procurado

an = a1 + r * (n - 1) #fórmula da P.A.
print("O %d termo é o valor %.1f" % (n, an))
