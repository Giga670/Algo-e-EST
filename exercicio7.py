N=int(input("digite um numero"))
N2=int(input("digite outro numero"))
N3=input("Digite 'A' para adição 'M' para multiplicação 'S' para subtração e 'D' para divisão")
if N3=="A":
    print(N+N2)
if N3=="M":
    print(N*N2)
if N3=="S":
    print(N-N2)
if N3=="D":
    print(N/N2) 