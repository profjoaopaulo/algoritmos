#questão 12 (Funções)

import random

def embaralhaTexto( texto ):
    texto = list(texto) #converte a string para lista
    random.shuffle(texto) #embaralha os elementos da lista 
    return ''.join(texto) #converte de lista para string

s = input("Digite um texto: ")
print( embaralhaTexto(s) )
