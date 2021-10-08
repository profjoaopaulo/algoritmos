#questão 03 (Funções)

#definição da função
def soma( n1, n2, n3 ):
    return n1 + n2 + n3

a = float( input("Digite um valor: ") )
b = float( input("Digite outro valor: ") )
c = float( input("Digite mais um valor: ") )

s = soma( a, b, c ) #chamada da função

print("Soma =", s)