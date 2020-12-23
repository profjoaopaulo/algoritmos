#ATIVIDADE STRINGS: questão d

texto = input("Digite um texto: ")

vogais = ['a', 'e', 'i', 'o', 'u']
substitutos = ['@', '3', '!', '0', '(']

for i in range(5): #serão 5 substituições
    texto = texto.replace(vogais[i], substitutos[i]) #lembre-se que replace() retorna uma cópia alterada

print(texto)
