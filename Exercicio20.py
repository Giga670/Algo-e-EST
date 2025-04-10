idade=(int(input("insira sua idade")))
membro=(input("você é membro"))
acompanhado=(input("está com um membro"))
if idade>=18:
    if membro=="sim":
        print("entrada liberada")
    elif acompanhado=="sim":
        print("pague meia entrada")
else:
    print=("não pode entrar")