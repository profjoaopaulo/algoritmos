area = float(input("Area em m2: "))

galoes = area // (3.6*6) #galões de 3,6L

if area % (3.6*6) > 0: #sobrou área a ser pintada?
	galoes = galoes + 1

print("Você precisa comprar %d galão(ões) e custará R$ %.2f" % (galoes, galoes*25))

