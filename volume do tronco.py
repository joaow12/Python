#exemplo 1

import math

Rmaior = float(input("Digite o valor do raio da base maior: "))
Rmenor = float(input("Digite o valor do raio da base menor: "))
h = float(input("Digite o valor da altura do tronco: "))

print ("o volume do tronco é: ",(math.pi*h)/3*(Rmaior**2+Rmaior*Rmenor+Rmenor**2))

