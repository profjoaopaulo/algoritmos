#ATIVIDADE STRINGS: questão c

texto = input("Digite um texto: ")

texto = texto.strip() #limpando quaisquer espaços em branco antes e depois da string

palavras = 0

if len(texto) > 0: #Se tiver ao menos um caractere, tem ao menos uma palavra
    palavras = 1

for i in range( len(texto) - 1 ): #verifica onde no espaço em branco se vem um caractere visível depois para contar mais uma palavra
    if texto[i].isspace() and not texto[i+1].isspace():
        palavras += 1

print("No texto digitado tem %d palavra(s)" % palavras)
