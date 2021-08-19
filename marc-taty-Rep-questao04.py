popA = 80000 #população inicial de A
popB = 200000 #população inicial de B
txA = 0.03 #taxa de crescimento anual da pop. de A
txB = 0.015 #taxa de crescimento anual da pop. de B
qtAnos = 0

while popA < popB:
	popA += popA * txA #crescimento da popA
	popB += popB * txB #crescimento da popB
	qtAnos += 1 #passou-se mais um ano
	
print("Passaram-se %d anos!" % qtAnos)

#A -> 80000 hab - 3% cresc. anual
#B -> 200000 hab - 1,5% cresc. anual


