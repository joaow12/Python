#exercicio 2 - aula 13

placa=[]
multa=[]
soma=0
valorMM=0

for i in range(5):
    placa.append (input("Digite a placa do carro: "))
    multa.append (float(input("Digite o valor da multa: ")))
    soma=multa[i]+soma
    if multa[i]>=300:
        valorMM=valorMM+1


print("O valor médio das multas é: ", soma/15,
      "\n O quantidade de multas acima de R$ 300:", valorMM)
      
    
    
