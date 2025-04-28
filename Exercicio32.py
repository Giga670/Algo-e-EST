def tabuada_personalizada(base, inicio, fim):
    print(f"tabuada do {base} do {inicio} a {fim}")
    for j in range(inicio, fim+1):
        print(f"{base} x {j} = {base*j}")
base=(int(input("insira a base da função")))
inicio=(int(input("insira o inicio da tabuada")))
fim=(int(input("insira o fim da tabuada")))
tabuada_personalizada(base,inicio,fim)