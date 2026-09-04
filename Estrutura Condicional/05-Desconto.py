import os
os.system("cls")

valor_compra = float(input("Digite o valor da compra: "))

if valor_compra >= 500:
    desconto = valor_compra * 0.10
else:
    desconto = 0

conta = valor_compra - desconto

print(f"O valor da compra é: R${valor_compra:.2f}")
print(f"Recebeu um desconto de: R${desconto:.2f}")
print(f"O produto final custou: R${conta:.2f}")