#Questão 13 (Funções)

#Definição da função que vai desenhar uma moldura
def desenhaMoldura( l, c ):    
    #Filtragem do l (linha) e c (coluna) para ficar entre 1 e 20
    if l < 1:
        l = 1
    elif l > 20:
        l = 20
    
    if c < 1:
        c = 1
    elif c > 20:
        c = 20

    for i in range(l):
        for j in range(c):
            if (i == 0 and j == 0) or (i == 0 and j == c-1) or (i == l-1 and j == 0) or (i == l-1 and j == c-1):
                print("+", end = "")
            elif i == 0 or i == l-1:
                print("-", end = "")
            elif j == 0 or j == c-1:
                print("|", end = "")
            else:
                print(" ", end = "")
        
        print()


linhas = int(input("Linhas: "))
colunas = int(input("Colunas: "))

desenhaMoldura(linhas, colunas)
