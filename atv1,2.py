N=input("nome")
C=input("cidade")
print=("N,C")

#2
num = float(input("Digite um número: "))
quadrado = num**2
raiz = num**0.5
print(f"Quadrado: {quadrado}")
print(f"Raiz quadrada: {raiz}\n")

#3
km = float(input("Digite um valor em quilômetros: "))
metros = km * 1000
centimetros = km * 100000
print(f"Equivalente em metros: {metros} m")
print(f"Equivalente em centímetros: {centimetros} cm\n")

#4
celsius = float(input("Digite a temperatura em °C: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"Temperatura em Fahrenheit: {fahrenheit}°F\n")

#5
ano_nascimento = int(input("Digite o ano de seu nascimento: "))
idade_2030 = 2030 - ano_nascimento
print(f"Em 2030 você terá {idade_2030} anos.\n")

#6
idade = int(input("Digite a sua idade: "))
if idade <= 12:
    print("Classificação: Criança\n")
elif idade <= 17:
    print("Classificação: Adolescente\n")
elif idade <= 59:
    print("Classificação: Adulto\n")
else:
    print("Classificação: Idoso\n")

#7
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
produto = n1 * n2 * n3
print(f"O produto total é: {produto}\n")

#8
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"Média final: {media:.1f}")
if media < 5:
    print("Situação: Reprovado")
elif media <= 6.9:
    print("Situação: Recuperação")
else:
    print("Situação: Aprovado")
