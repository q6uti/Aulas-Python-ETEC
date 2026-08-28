import os
os.system("cls")


peso = float(input("Digite seu peso:  "))
altura = float(input("Digite sua altura:  "))
print("")

IMC = peso / (altura ** 2)

print(f"Seu IMC, é de: {IMC:.2f}")

input("Precione Enter para finalizar o proramaga...")
