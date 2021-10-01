#questão 08 - Strings
frase = input("Digite uma frase e veja se é palíndromo: ")

frase = frase.replace(" ", "") #retira os espaços em branco
tam = len(frase)
j = tam - 1
ehPalindromo = True

for i in range(tam//2):
    if frase[i] != frase[j]: #se os caracteres em oposição são diferentes, não é palíndromo!
        ehPalindromo = False
        break
    
    j -= 1

print(frase)
if ehPalindromo:
    print("É palíndromo!")
else:
    print("Não é palíndromo!")

