import os
os.system("cls")

nome = input("Insira seu nome: ")
vendas = float(input("Valor das vendas: "))

if vendas > 20.000:
    comissao = vendas / 10