#questão c: Atividade 'ESTRUTURAS DE CONTROLE: DECISÃO E REPETIÇÃO'

a = []
b = []
s = []

print("Digite 5 valores reais para o vetor A:")
for i in range(5):
    a.append( float(input()) )

print("Digite 5 valores reais para o vetor B:")
for i in range(5):
    b.append( float(input()) )

#Armazenando as somas no vetor S
for i in range(5):
    s.append( a[i] + b[i] )

print("vetor S: ", s)


