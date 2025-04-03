produto=(input("insira o nome do produto"))
preco=(float(input("insira o preço")))
quantidade=(int(input("insira a quantiadade")))
precototal=preco*quantidade
if precototal>100:
    precototal=precototal/0.95
    print(f"{quantidade} {produto}s vai custar {precototal} reais")
else:
    print(f"{quantidade} {produto}s vai custar {precototal} reais")