palavras=[]
for i in range(0,5):
    palavras.append(input("insira uma palavra"))
poli=[]
for i in range(0,5):
    if palavras[i][::-1]==palavras[i]:
        poli.append(palavras[i])
print(f"estas são as palavras Palíndromos {poli}")