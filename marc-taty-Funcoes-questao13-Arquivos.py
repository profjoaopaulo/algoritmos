#ARQUIVOS EM PYTHON

def desenhaMoldura( l, c ):
    lista = [] #lista para armazenar os caracteres da moldura
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
                lista.append("+") #usando append() para adicionar os caracteres na lista
            elif i == 0 or i == l-1:
                lista.append("-")
            elif j == 0 or j == c-1:
                lista.append("|")
            else:
                lista.append(" ")
        
        lista.append("\n") #caractere 'pula linha' adicionado na lista

    #print(lista) #para verificar como fica a lista

    return lista #retorna a lista contendo os caracteres da moldura

#substitua o caminho do arquivo para um diretório válido no seu computador!
arquivo = open("/home/joao/Codes/AulasADS/exemplo.txt", "w") #abre arquivo com permissão de escrita 'w'

linhas = int(input("Linhas: "))
colunas = int(input("Colunas: "))

l = desenhaMoldura(linhas, colunas)

arquivo.write( "".join(l) ) #transformação dos elementos da lista em string e escrita da mesma no arquivo

arquivo.close() #não esqueça de fechar o arquivo!