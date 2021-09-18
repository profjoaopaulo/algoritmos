perguntas = ["Telefonou para a vitima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou coma vítima"]
contadorSuspeita = 0 #contador

for i in range(5): #i: 0, 1, 2, 3 e 4
    resposta = input( perguntas[i] ) #supor respostas 'sim' ou 'não'
    if resposta == "sim":
        contadorSuspeita += 1

if contadorSuspeita <= 1: #0 ou 1
    print("A pessoa é Inocente!")
elif contadorSuspeita == 2:
    print("A pessoa é Suspeita!")
elif contadorSuspeita <= 4: #3 ou 4
    print("A pessoa é Cúmplice!")
else: #5
    print("A pessoa é o Assassino!")



