tamanho = float( input("Tamanho do arquivo em MB: ") )
velocidade = float( input("Velocidade da Internet em Mbps: ") )

tempoDownload = ( (tamanho*8) / velocidade ) / 60

print("O download será feito em ", tempoDownload, " minutos!")

