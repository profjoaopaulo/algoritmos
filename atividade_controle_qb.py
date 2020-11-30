#questão b: Atividade 'ESTRUTURAS DE CONTROLE: DECISÃO E REPETIÇÃO'

x = float(input("x: "))
y = float(input("y: "))
z = float(input("z: "))

print("Calcular qual média?\nDigite:\n1 - para Geométrica\n2 - para Ponderada")
print("3 - para Harmônica\n4 - para Aritmética")
opcao = int(input())

if opcao == 1:
    print( "Média Geométrica = %.2f" % (x*y*z) ** (1/3) ) #raíz cúbica equivale a elevar a 1/3
elif opcao == 2:
    print( "Média Ponderada = %.2f" % ((x + 2*y + 3*z ) / 6) )
elif opcao == 3:
    print( "Média Harmônica = %.2f" % (3 / (1/x + 1/y + 1/z)) )
else:
    print( "Média Aritmética = %.2f" % ((x+y+z) / 3) )

#Observação: x, y ou z não podem ser zero, pois há divisões em que eles são denominadores
#Sinta-se livre para implementar que não permita divisão por zero