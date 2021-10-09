#questão 08 (Funções)

def informaDigitos(numero):
    numero = str(numero) #conversão para string
    return len(numero) #retorna a quantidade de caracteres (dígitos)

n = int( input("Digite um número: ") )

print("O número digitado tem %d dígitos!" % informaDigitos(n))
