#Questão C da Atividade de Estrutura Sequencial
sal_min = float(input("Valor do salário: "))
gasto_kw = float(input("Consumo em kW: "))

valor_1kW = (sal_min / 7) / 100
conta = gasto_kw * valor_1kW
conta_desconto = conta * 0.9

print("O valor de 1kW: R$ %.2f" % valor_1kW)
print("Conta R$ %.2f" % conta)
print("Pagando em dia, fica no valor de R$ %.2f" % conta_desconto)
