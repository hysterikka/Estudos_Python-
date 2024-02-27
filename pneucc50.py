import math
n = (int (input ("Digite o valor da pressao do pneu:")))
if n < 1 and n > 40:
    print ("Valor inválido")
else:
    m =(int (input ("Digite o valor da pressao desejada do pneu:")))
    if m < 1 and m < 40:
        print ("Valor inválido")
    else:
        print ("A pressao desejada é",m,".")
        d = int (n - m)
        print ("A diferenca é", d,".")