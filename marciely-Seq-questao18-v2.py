tamanho = float(input("Digite o tamanho em MB: "))
velocidade = float( input("Digite a velocidade em Mbps: ") )

tamanho = tamanho * (1024*1024) * 8 #bits
velocidade = velocidade * (1024*1024) #bits

tempo = tamanho / velocidade #segundos

minutos = tempo // 60
segundos = tempo % 60

#print("Velocidade em minutos: ", tempo/60)

if segundos < 10:
	print("0%d:0%d" % (minutos, segundos))
else:
	print("0%d:%d" % (minutos, segundos))
