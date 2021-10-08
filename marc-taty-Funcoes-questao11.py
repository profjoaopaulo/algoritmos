#questão 11 (Funções)
def mesPorExtenso( data ):
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    numerosData = data.split('/')
    return numerosData[0] + " de " + meses[ int(numerosData[1]) - 1 ] + " de " + numerosData[2]

date = input("Digite uma data DD/MM/AAAA: ")
dataExtenso = mesPorExtenso( date )
print( dataExtenso )

#07/10/2021
#numerosData = [7, 10, 2021] -> numerosData[1]
