alunos = []
numAlunos = 3 #configure aqui o número de alunos
medias = []
numAlunosMediaMaiorQue7 = 0 #contador

for i in range(numAlunos): #roda o número de alunos
    soma = 0 #reseta a soma
    notas = [] #reseta a lista notas
    for j in range(4): #roda o número de notas 
        print("Digite a nota %d para o aluno %d" % (j, i))
        nota = float( input("Digite uma nota de 0 a 10: ") )
        notas.append(nota)
        soma += nota #soma = soma + nota
    
    media = soma / 4
    if media >= 7:
        numAlunosMediaMaiorQue7 += 1 #numAlunosMediaMaiorQue7 = numAlunosMediaMaiorQue7 + 1
    medias.append(media)

    alunos.append( notas )

print(alunos)
print(medias)
print("São %d alunos com média >= 7" % numAlunosMediaMaiorQue7)

#Exemplos abaixo
#alunos = [ [10, 9, 7, 1], [8, 6, 4, 2], [1, 2, 3, 4], [], ..., [] ]
#alunos[0][1] == 9 #acesso ao valor 9
#alunos[1][2] == 4 #acesso ao valor 4
#medias = [6,75, ..., ]