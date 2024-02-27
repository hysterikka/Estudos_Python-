import math

# Função para verificar se a idade está no intervalo [5, 100]
def verificar_intervalo(idade):
    return 5 <= idade <= 100

# Solicitar e verificar a primeira idade
idade1 = int(input("Insira a primeira idade: "))
while not verificar_intervalo(idade1):
    print("A idade deve estar no intervalo [5, 100]. Tente novamente.")
    idade1 = int(input("Insira a primeira idade: "))

# Solicitar e verificar a segunda idade
idade2 = int(input("Digite a segunda idade: "))
while not verificar_intervalo(idade2):
    print("A idade deve estar no intervalo [5, 100]. Tente novamente.")
    idade2 = int(input("Digite a segunda idade: "))

# Solicitar e verificar a terceira idade
idade3 = int(input("Digite a terceira idade: "))
while not verificar_intervalo(idade3):
    print("A idade deve estar no intervalo [5, 100]. Tente novamente.")
    idade3 = int(input("Digite a terceira idade: "))

# Verificar as condições
if (idade3 < idade1) and (idade1 < idade2):
    print(idade1)
elif (idade1 > idade3) and (idade1 > idade2):
    print(idade1)
elif (idade2 < idade1) and (idade2 > idade3):
    print(idade2)
elif (idade1 < idade2) and (idade2 < idade3):
    print(idade2)
elif (idade3 > idade1) and (idade3 == idade2):
    print(idade3)
elif (idade3 > idade2) and (idade3 == idade1):
    print(idade3)
