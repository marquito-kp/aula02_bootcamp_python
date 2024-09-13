# Exercicios aula 2
# Números de Ponto Flutuante (float)

# 1) Escreva um programa que receba dois números flutuantes e realize sua adição.

#num1 = float(input("Digite um número: "))
#num2 = float(input("Digite outro número: "))

#soma = num1 + num2

#print(f"A soma de {num1} e {num2} é {soma}")

# 2) Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# num = []

# O método append ao ser invocado ele adiciona um elemento ao final da lista do array mencionado
# No caso em questão o append é invocado quando é solicitado um número ao usuário, desta forma inserindo o número no array num


# num.append(float(input("Digite um número: ")))
# num.append(float(input("Digite outro número: ")))

# O método sum() realiza a soma de todos os elementos de um array, 
# já o método len() retorna o número de elementos contidos em um array

# Desta forma, ao invocar o método sum() ele soma todos os número do arry num, 
# enquanto o len() retonar o número de elementos no array num

# soma = sum(num)
# media = soma/len(num)

# print(f"A média dos números inseridos é {media}")

# 3) Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# base = float(input("Insira a base da pontência: "))
# expoente = float(input("Insira o expoente da pontência: "))

# pontencia = base ** expoente

# print(f"O resulta da pontência é de {pontencia}")

# 4) Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# celsius = float(input("Digite a temperatura em celsius: "))

# fahrenheit = celsius * 1.8 + 32

# print(f"A temperatura em celsius {celsius} é igual a {fahrenheit} fahrenheit.")

# 5) Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

raio = float(input("Digite o raio do circulo: "))

pi = 3.1415
area_circulo = pi * (raio**2)

print(f"O raio do circulo {raio} resulta na área de {area_circulo}")