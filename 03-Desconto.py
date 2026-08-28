import os
os.system("cls")


print("╭───────────────────────────────────────────────────╮")
print("│             CALCULADORA DE DESCONTO               │")
print("╰───────────────────────────────────────────────────╯")
print("")

# Solicita o nome do produto ao usuário e guarda como texto;
produto = input("Informe o nome do produto: ")

# Solicita o preço, converte o texto para número decimal e guarda na variável;
valor = float(input("Informe o preço do produto:  "))

# Solicita a porcentagem de desconto, converte para decimal e guarda na variável;
desconto = float(input("Digite o quanto de desconto deseja: "))


# Calcula o valor em dinheiro que será abatido com base na porcentagem;
valor_desconto = valor * (desconto / 100)

# Subtrai o desconto do preço original para encontrar o preço final a pagar;
valor_final = valor - valor_desconto


# Mostra o resultado para o usuário;
print("")
print(f"» Produto:    {produto}")
print(f"» Desconto:   {desconto}% | (-R$ {valor_desconto:.2f})")
print(f"» Valor Final: R$ {valor_final:.2f}")
print("")
input("Precione Enter para finalizar o proramaga...")