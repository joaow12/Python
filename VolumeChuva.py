#exercicio 1 - aula 12

dias=[]
volume=[]
soma=0
somaQ=0
Qtde=0

for i in range(10):
    dias.append(input("Dite o dia da semana: "))
    volume.append(float(input("Digite o volume de chuva: ")))

for valor in volume:
    soma=soma+valor

for i in range(10):
    if dias[i] == "quarta feira" or dias[i] == "Quarta" or dias[i] == "quarta" or dias[i] == "qua":
        somaQ=somaQ+volume[i]
        Qtde=Qtde+1

print("O volume médio de chuva na quarta feira é: ", (somaQ/Qtde),
"\nO volume total é: ", soma)
