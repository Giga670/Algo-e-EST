numeros=[]
for i in range(1,6):
    numeros.append (int(input("escreva um numero inteiro")))
maior=numeros[0]
menor=numeros[0]
for e in range (1,5):
    if numeros[e]>maior:
        maior=numeros[e]
print(maior)
for e in range (1,5):
    if numeros[e]<menor:
        menor=numeros[e]
print(menor)