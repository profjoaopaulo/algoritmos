#questão 21 em: https://wiki.python.org.br/EstruturaDeRepeticao 

x = int( input("Digite um inteiro: ") )

ehPrimo = True #flag
for i in range(2, x):
    if x % i == 0:
        ehPrimo = False
        print("Não é primo!")
        break

if ehPrimo:
    print("É primo!")
