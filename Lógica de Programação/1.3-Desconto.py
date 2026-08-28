import os
os.system("cls")


# Entrada
nome_produto = input("Digite o nome do produto: ")

valor_produto = float(input("Informe o preço do produto: "))
proc_desconto = float(input("Digite o desconto do produto: "))

# Processamento
total = valor_produto - (valor_produto * proc_desconto ) / 100

# Saída
print(f"O valor do {nome_produto}, com desconto é {total}")
input("Precione Enter para finalizar o proramaga...")
