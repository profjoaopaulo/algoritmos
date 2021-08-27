n = int(input("Digite o n-esimo termo, sendo n >= 3: "))

print("1 1", end = " ")

a = 1
b = 1

for i in range(n-2):
	x = a + b
	print(x, end = " ")
	a = b
	b = x

print()
#Desafio: fazer uma versão deste problema usando o laço WHILE!
