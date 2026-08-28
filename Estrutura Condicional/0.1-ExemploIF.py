import os
os.system("cls")

nascimento = int(input("Informe seu ano de nascimento: "))
atual = int(input("Informe o ano atual: "))

a1 = nascimento - nascimento

if a1 > 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
