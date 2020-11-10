#Questão 04 em https://wiki.python.org.br/EstruturaDeRepeticao

#A: 80000 hab / txA = 3% a.a.
#B: 200000 hab / txB = 1,5% a.a.

pa = 80000
pb = 200000

qtAnos = 0

#a cada iteração do laço, passa-se 1 ano e aumenta a população
while pa < pb: #vai sair do laço quando a população de A for igual ou maior que B
    pa += pa*0.03 #pa = pa + pa*0.03
    pb += pb*0.015
    qtAnos += 1

print("Quantidade de anos em que pa >= pb: ", qtAnos)
print("População de A: %.2f" % pa)
print("População de B: %.2f" % pb)
