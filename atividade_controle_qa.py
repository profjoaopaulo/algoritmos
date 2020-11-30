#questão a: Atividade 'ESTRUTURAS DE CONTROLE: DECISÃO E REPETIÇÃO'

import math #para uso da função sqrt() 'raiz quadrada'

a = float(input("coeficiente a: ")) #a != 0
b = float(input("coeficiente b: "))
c = float(input("coeficiente c: "))

delta = b**2 - 4*a*c

if delta > 0: #haverá duas raízes reais x1 e x2
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("x1 = %.2f e x2 = %.2f" % (x1, x2))
elif delta == 0: #haverá apenas uma raiz real x1==x2
    x = -b / (2*a)
    print("x = %.2f" % x)
else: #delta < 0: não há raiz real (solução não pertence ao conjunto dos Reais)
    print("Sem raíz real!")
