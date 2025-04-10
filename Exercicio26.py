notas=[]
media=0
for i in range(1,6):
    notas.append(float(input("digite uma nota")))
for e in range(0,5):
    media=media+notas[e]
media=media/len(notas)
print(media)