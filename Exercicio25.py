num=12
palpites=[]
sorte=0
while sorte!=12:
    sorte=0
    sorte=(int(input("digite um numero")))
    if sorte!=12:
        palpites.append (sorte)
if sorte==12:
    print(palpites)
    print(f"parabens voce acertou o {num}, foram necesarias {len(palpites)} tentativas")