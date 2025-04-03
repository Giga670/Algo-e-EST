idade=(int(input("insira sua idade")))
sexo=(input("qual seu genero"))
if sexo=="masculino":
    atleta=(input("você é atleta"))
if idade<15:
    print("propaganda de artigos infantis")
elif idade>15 and idade<21 and sexo=="feminino":
    print("propaganda de artigos de maquiagem e moda")
elif idade>15 and idade<32 and sexo=="masculino" and atleta=="sim":
    print("propaganda de artigos esportivos")
else:
    print("propagandas variadas")
