def tabuada(numero):
    print(f"tabuada do {numero}:")
    for i in range(1,11):
        print(f"{numero} X {i} = {numero*i}")
tabuada(int(input("insira um numero")))
