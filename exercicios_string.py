# Exercícios Aula 02
# Strings (str)
# 1) Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

#string = str.upper((input("Digite uma palavra: ")))

#print(string)
 
# 2) Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# string = str.lower((input("Digite uma palavra: ")))

# print(string)

# 3) Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase 
# sem espaços em branco no início e no final.

#string = str.strip((input("Digite uma frase: ")))

#print(string)

# 4) Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

#string = str((input("Digite uma data no formato dd/mm/aaaa: ")))

#sep = "/"

#print(string.split(sep))


# 5) Escreva um programa que concatene duas strings fornecidas pelo usuário.

string1 = str(input("Digite uma palavra: "))
string2 = str(input("Digite outra palavra: "))

print(string1+" "+string2)