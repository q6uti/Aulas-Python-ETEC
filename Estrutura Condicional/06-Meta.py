import os
os.system("cls")

nome = input("Insira seu nome: ")
vendas = float(input("Quantas vendas você fez durante o mês: "))

if vendas > 15.000:
    print(f"Excelente! {nome}")
elif vendas > 10.000:
    print("Meta atingida.")
else:
    print("Meta não atingida :(")