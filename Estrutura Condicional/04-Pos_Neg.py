import os
os.system("cls")

num = float(input("Insira um numero qualquer: "))

if num > 0:
    print("Seu número é positivo!")
elif num < 0:
    print("Seu número é negativo!")
else:
    print("Seu número é igual a zero.")