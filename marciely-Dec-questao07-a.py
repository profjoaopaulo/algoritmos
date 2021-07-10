a = float( input("Digite um número: ") )
b = float( input("Digite mais um número: ") )
c = float( input("Digite mais um número: ") )

if a == b and a == c:
	print("É o mesmo valor:", a)
else:
	#Maior
	if a > b: #SE
		if a > c:
			print("%f é o maior valor" % a)
		else:
			print("%f é o maior valor" % c)
	elif b > c: #SENÃO-SE
		print("%f é o maior valor" % b)
	else: #SENÃO
		print("%f é o maior valor" % c)
	
	#Menor
	if a < b:
		if a < c:
			print("%f é o menor valor" % a)
		else:
			print("%f é o menor valor" % c)
	elif b < c:
		print("%f é o menor valor" % b)
	else:
		print("%f é o menor valor" % c)


	

	

