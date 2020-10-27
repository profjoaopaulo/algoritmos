#Questão 05 em https://wiki.python.org.br/EstruturaDeDecisao
nota1 = float(input("Digite nota 1: "))
nota2 = float(input("Digite nota 2: "))

media = (nota1+nota2)/2

if media == 10:
	print("Aprovado com Distinção com média %.2f" % media)
elif media >= 7:
	print("Aprovado com média %.2f" % media)
else:
	print("Reprovado com média %.2f" % media)

	
