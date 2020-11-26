#exercicio 2

Sbruto = int(input("Digite o salário bruto do funcionário: "))
Sliquido = Sbruto-Sbruto*0.11

if Sliquido<1000:
    print("O salário bruto é: ", Sbruto)
    print("O salário líquido é: ",Sliquido)
    print("A gratificação é: 200")
    print("O salário líquido mais a gratificação é: ", Sliquido+200)
elif Sliquido>=1000 and Sliquido<=1250:
    print("O salário bruto é: ", Sbruto)
    print("O salário líquido é: ",Sliquido)
    print("A gratificação é: 150")
    print("O salário líquido mais a gratificação é: ", Sliquido+150)
elif Sliquido>=1250 and Sliquido<1750:
    print("O salário bruto é: ", Sbruto)
    print("O salário líquido é: ",Sliquido)
    print("A gratificação é: 100")
    print("O salário líquido mais a gratificação é: ", Sliquido+100)
elif Sliquido>=1750:
    print("O salário bruto é: ", Sbruto)
    print("O salário líquido é: ",Sliquido)
    print("A gratificação é: 75")
    print("O salário líquido mais a gratificação e: ", Sliquido+75)

