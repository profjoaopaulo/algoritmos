#questão 01 (Arquivos)

#Função que valida o IP - Retorna True (IP válido) ou False (IP inválido)
def validaIP( ip ):
    ehValido = True
    numeros = ip.split(".")
    for i in range( len(numeros) ):
        n = int( numeros[i] )
        if n < 0 or n > 255:
            ehValido = False
            break

    return ehValido


#Programa Principal
arquivoEntrada = open("entrada.txt", "r")

ips = arquivoEntrada.readlines() #readLines() ler todo o conteúdo do arquivo e armazena numa lista

ipsValidos = []
ipsInvalidos = []

#print(ips)

for i in range( len(ips) ):
    if validaIP( ips[i] ): #IP é válido?
        ipsValidos.append( ips[i] ) #IP válido sendo armazenado na lista
    else:
        ipsInvalidos.append( ips[i] ) #IP inválido sendo armazenado na lista

#montando uma lista com todo o conteúdo do arquivo de saída
conteudoSaida = []
conteudoSaida.append("[Endereços válidos:]\n")
conteudoSaida.extend( ipsValidos )
conteudoSaida.append("\n\n")
conteudoSaida.append("[Endereços inválidos:]\n")
conteudoSaida.extend( ipsInvalidos )

arquivoSaida = open("saida.txt", "w") #abrindo o arquivo para escrever
arquivoSaida.write( "".join( conteudoSaida ) )

arquivoEntrada.close()
arquivoSaida.close()