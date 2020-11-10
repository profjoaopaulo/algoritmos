#Questão 13 em https://wiki.python.org.br/EstruturaDeDecisao 

dia = int(input("Digite o dia da semana: "))

if dia >= 1 and dia <= 7:
    if dia == 1:
        print("Domingo")
    elif dia == 2:
        print("Segunda")
    elif dia == 3:
        print("Terça")
    elif dia == 4:
        print("Quarta")
    elif dia == 5:
        print("Quinta")
    elif dia == 6:
        print("Sexta")
    else:
        print("Sábado")
else:
    print("Dia inválido")

#Desafio: consegue fazer uma nova versão desse algoritmo usando Listas?
#O objetivo é diminuir a quantidade de if/elif/else
    
