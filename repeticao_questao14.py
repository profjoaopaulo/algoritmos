#questão 14 em: https://wiki.python.org.br/EstruturaDeRepeticao 

contPares = 0
contImpares = 0

for i in range(10):
    x = int(input("Digite um valor inteiro: "))
    if x % 2 == 0:
        contPares += 1
    else:
        contImpares += 1

print("Pares: ", contPares)
print("Ímpares: ", contImpares)
