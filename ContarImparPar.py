#exercicio 1 - aula 13

resp = "s"
valores=[]
impar=[]
par=[]
qtde=0
qtdeP=0
qtdeI=0

while resp=="s" or resp=="S":
    n = int(input("Dite um número: "))
    valores.append(n)
    resp = input("Deseja continuar? ")
    qtde=qtde+1
    if n%2==0:
        qtdeP=qtdeP+1
        par.append(n)
    else:
        qtdeI=qtdeI+1
        impar.append(n)

print("Quantidade de números Impares é: ",qtdeI, impar,
      "\n Quantidade de números Pares é: ",qtdeP, par,
      "\n Quantiadde de números é: ",qtde, valores)
