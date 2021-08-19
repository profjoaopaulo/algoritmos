data = input("Digite a data no formato dd/mm/aaaa: ")

dia, mes, ano = data.split("/")

#conversão para inteiro
dia = int(dia)
mes = int(mes)
ano = int(ano)

flag = "Válido!"

if ano < 1 or ano > 9999:
	flag = "Inválido!"
elif mes < 1 or mes > 12:
	flag = "Inválido!"
elif dia >= 1: #o dia parece válido...
	if dia > 31:
		flag = "Inválido!"
	elif dia == 31 and (mes == 2 or mes == 4 or mes == 6 or mes == 9 or mes == 11):
		flag = "Inválido!"
	elif dia == 30 and mes == 2:
		flag = "Inválido!"
	elif dia == 29 and mes == 2:
		if (ano % 4 != 0) or (ano % 100 == 0 and ano % 400 != 0):
			flag = "Inválido!"

print(flag)

#dia == 29 and mes == 2 and (ano % 4 != 0):


