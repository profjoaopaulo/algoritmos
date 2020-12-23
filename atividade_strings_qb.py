#ATIVIDADE STRINGS: questão b

texto = input("Digite um texto que possa conter números...: ")

contador = 0

for i in texto: #a variável i recebe cada caractere do texto
    if i.isnumeric():
        contador += 1

print("No texto digitado tem %i número(s)" % contador)