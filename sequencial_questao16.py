#https://wiki.python.org.br/EstruturaSequencial 
#Questão 16

tamanhoArea = float( input("Digite a área a ser pintada em m2: ") )

#Dividindo área a ser pintada pela área que pode ser pintada com uma lata (54m2)
latas = tamanhoArea / 54 

print("A quantidade de latas necessárias é: ", latas)

valorPagar = latas * 80 #Cada lata de 18L custa R$ 80,00

print("O valor a ser pago pelas %.1f lata(s) será de R$ %.2f reais" % (latas, valorPagar) )

###NOTA: não encontrei uma maneira de resolver a questão da fração de uma lata que não pode ser vendida
###Exemplo, se pintar 81 m2, vamos precisar de 1,5 lata (uma lata e meia) e ele deveria comprar duas latas!
###Mas essa situação só poderá ser resolvida melhor com os comandos de decisão a serem mostrados no proximo conteúdo.


#1 litro <-> pintar 3 m2
#lata 18l <-> R$ 80,00
#Saídas: qt latas; R$ preço total
