#ATIVIDADE STRINGS: questão e

texto = input("Digite um texto: ")

soma = 0

for i in texto:
    soma += ord(i) - 96 #a função ord() retorna o código caractere em ASCII de cada caractere. Para 'a' ser o peso 1, 'b' o peso 2 e assim sucessivamente, basta subtrair 96 de cada

print(soma)
