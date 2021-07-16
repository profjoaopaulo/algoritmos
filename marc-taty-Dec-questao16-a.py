import math

a = float( input("a: ") )
b = float( input("b: ") )
c = float( input("c: ") )

if a == 0:
	print("Não temos uma equação do 2º grau!")
else: #a != 0
	delta = b**2 - 4*a*c
	if delta < 0:
		print("Não existe raízes reais!!!")
	elif delta == 0:
		x = -b / (2*a)
		print("Uma única raiz real:", x)
	else: #delta > 0
		raizDelta = math.sqrt(delta)
		x1 = (-b + raizDelta) / (2*a)
		x2 = (-b - raizDelta) / (2*a)
		print("x' =", x1)
		print("x'' =", x2)
		
		
		
		
