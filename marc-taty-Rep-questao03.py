#Admite-se no início que as entradas estão erradas
vnome = False
vidade = False
vsalario = False
vsexo = False
vestadoCivil = False

#estratégia de repetição enquanto houver entrada errada
while True:

	#Pede-se as entradas, e repete as que houver erro
	if vnome == False:	
		nome = input("Nome: ");
		vnome = True	
	if vidade == False:
		idade = int( input("Idade: ") )
		vidade = True		
	if vsalario == False:
		salario = float( input("Salário: ") )
		vsalario = True		
	if vsexo == False:
		sexo = input("Sexo: ")
		vsexo = True		
	if vestadoCivil == False:
		estadoCivil = input("Estado civil: ")
		vestadoCivil = True
	
	#Testes para verificar se há entrada inválida
	if len(nome) <= 3:
		vnome = False
	if idade < 0 or idade > 150:
		vidade = False		
	if salario <= 0:
		vsalario = False		
	if sexo != 'f' and sexo != 'm':
		vsexo = False
	if estadoCivil != 's' and estadoCivil != 'c' and estadoCivil != 'v' and estadoCivil != 'd':
		vestadoCivil = False

	if vnome == True and vidade == True and vsalario == True and vsexo == True and vestadoCivil == True:
		break
		
print(nome)
print(idade)
print(salario)
print(sexo)
print(estadoCivil)

