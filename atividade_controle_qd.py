#questão d: Atividade 'ESTRUTURAS DE CONTROLE: DECISÃO E REPETIÇÃO'

while True:
    print("Digite dois valores reais:")
    a = float(input())
    b = float(input())

    while True: #laço para avaliar a opção escolhida após leitura dos valores
        print("CALCULADORA PYTHON – OPÇÕES:\nDigite Add para somar;\nDigite Sub para subtrair;")
        print("Digite Prod para multiplicar;\nDigite Div para dividir;\nDigite Sair para encerrar o programa.")

        opcao = input()

        if opcao == "Add" or opcao == "Sub" or opcao == "Prod" or opcao == "Div" or opcao == "Sair":
            break #Sai do laço pois a opção foi válida
        else:
            print("Opção Inválida! Tente novamente!")
            continue #Continua no laço pois a opção está inválida


    if opcao == "Add":
        print("(SOMA) %.2f + %.2f = %.2f" % (a, b, a+b))
        continue
    elif opcao == "Sub":
        print("(SUBTRAÇÃO) %.2f - %.2f = %.2f" % (a, b, a-b))
        continue
    elif opcao == "Prod":
        print("(MULTIPLICAÇÃO) %.2f * %.2f = %.2f" % (a, b, a*b))
        continue
    elif opcao == "Div":
        print("(DIVISÃO) %.2f / %.2f = %.2f" % (a, b, a/b))
        continue
    elif opcao == "Sair":
        break #Sai do laço principal e encerra o programa

