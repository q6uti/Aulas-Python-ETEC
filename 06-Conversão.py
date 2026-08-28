import os
os.system("cls")


valor_dolar = float(input("Digite o valor em dólares (US$): "))
cotacao_dolar = float(input("Digite a cotação do dólar (R$): "))

total_reais = valor_dolar * cotacao_dolar

print(f"US$ {valor_dolar:.2f} equivale a R$ {total_reais:.2f}")

input("Precione Enter para finalizar o proramaga...")