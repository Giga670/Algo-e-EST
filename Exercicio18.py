salariabase=(float(input("insira seu salario base")))
horasextras=(float(input("insira as horas extras")))
valorextra=(float(input("insira o valor por hora extra")))
extra=valorextra*horasextras
salariototal=salariabase+extra
print(f"você deve receber {salariototal} reais ")