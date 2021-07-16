a = float( input("Digite um valor: ") ) 
b = float( input("Digite outro valor: ") )
c = float( input("E digite mais um valor: ") )


if a > b:
	if a > c: #Se verdadeiro, a é o maior
		if b > c: #Se verdadeiro, c é o menor
			print(a, b, c)
		else:
			print(a, c, b)
	else: #Se verdadeiro, c é o maior e b o menor
		print(c, a, b)
elif b > c: #Se verdadeiro, b é o maior
	if a > c: #Se verdadeiro, c é o menor
		print(b, a, c)
	else:
		print(b, c, a)
else: #Se verdadeiro, c é o maior e o a é o menor
	print(c, b, a)
	
	
	
	
	
