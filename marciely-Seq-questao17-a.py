area = float(input("Area em m2: "))

latas = area // (18*6) #latas de 18L

if area % (18*6) > 0: #sobrou área a ser pintada?
	latas = latas + 1

print("Você precisa comprar %d lata(s) e custará R$ %.2f" % (latas, latas*80))

