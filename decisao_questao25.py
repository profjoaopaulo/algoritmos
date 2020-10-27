#Questão 25 em https://wiki.python.org.br/EstruturaDeDecisao
question1 = input("Telefonou para a vítima (sim ou não)?: ")
question2 = input("Esteve no local do crime (sim ou não)?: ")
question3 = input("Mora pero da vítima (sim ou não)?: ")
question4 = input("Devia para vítima (sim ou não)?: ")
question5 = input("Já trabalhou com a vítima (sim ou não)?: ")

numeroSim = 0 #nosso contador de sims

if question1 == "sim":
	numeroSim = numeroSim + 1

if question2 == "sim":
	numeroSim = numeroSim + 1

if question3 == "sim":
	numeroSim = numeroSim + 1

if question4 == "sim":
	numeroSim = numeroSim + 1
	
if question5 == "sim":
	numeroSim = numeroSim + 1

	
if numeroSim == 5:
	print("Assassino!")
elif numeroSim == 3 or numeroSim == 4:
	print("Cúmplice!")
elif numeroSim == 2:
	print("Suspeito!")
else:
	print("Inocente!")








