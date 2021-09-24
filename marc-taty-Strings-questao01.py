#questão 01 (Strings)
s1 = input("Digite um pequeno texto: ")
s2 = input("Digite um outro pequeno texto: ")

print(s1, len(s1), " caracteres")
print(s1, len(s2), " caracteres")

if len(s1) == len(s2):
    print("As duas strings possuem o mesmo tamanho!")
else:
    print("As duas strings possuem tamanho diferentes!")

if s1 == s2:
    print("São iguais!")
else:
    print("São diferentes!")
