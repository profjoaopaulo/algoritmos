valorHora = float( input("Quanto vc ganha por hora? ") )
horasTrab = float( input("Quantas horas vc trabalhou? ") )

salBruto = valorHora * horasTrab #salário bruto
ir = salBruto * 0.11 #IR
inss = salBruto * 0.08 #INSS
sind = salBruto * 0.05 #Sindicato
saLiq = salBruto - ir - inss - sind #salário líquido


#print("+ Salario Bruto : R$ %.2f\n- IR (11%) : R$ %.2f\n- INSS (8%) : R$ %.2f\n- Sindicato (5%) : R$ %.2f\n= Salario Liquido : R$ %.2f" % (salBruto, ir, inss, sind, saLiq))

print("bruto: R$ ", salBruto)
print("IR: R$ ", ir)
print("INSS: R$ ", inss)
print("Sindicato: R$ ", sind)
print("Líquido: R$ ", saLiq)
