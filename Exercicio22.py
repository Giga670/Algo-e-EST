palavras=[]
maior5=0
for i in range(0,6):
    palavras.append (input("digite uma palavra"))
for e in range(0,6):
    if len(palavras[e])>=5:
        maior5=maior5+1
print(maior5)