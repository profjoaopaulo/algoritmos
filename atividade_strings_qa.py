#ATIVIDADE STRINGS: questão a

texto = input("Digite um texto: ")
vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for i in range(len(texto)):
    if texto[i] in vogais: #o operador in verifica a existência do caractere no grupo de vogais
        print(texto[i].upper(), end = "") #sendo o caractere uma vogal, converter para maiúsculo
    else:
        print(texto[i], end = "") #não é vogal, imprime do jeito qe está

print()