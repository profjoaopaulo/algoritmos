#questão 13 em: https://wiki.python.org.br/EstruturaDeRepeticao 

base = float(input("Digite a base: "))
exp = float(input("Digite o expoente: "))

i = 1
res = 1
while i <= exp:
    res *= base
    i += 1

print("resultado: ", res)
