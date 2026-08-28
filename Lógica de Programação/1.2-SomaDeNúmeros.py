import os
os.system("cls")


print("=========================\           Super Calculadora Pro Max            /=========================")
#   Passo 1    -   Entrada de Dados
nome = input("Informe seu nome: ")

numero1 = int(input("Informe o primeiro valor:  "))
numero2 = int(input("Informe o segundo  valor:  "))

print("")

#   Passo 2    -   Processamento
total = numero1 + numero2


#   Passo 3    -   Saída
print(f"Olá {nome}, seu resultado deu {total}")

input("Precione Enter para finalizar o proramaga...")
