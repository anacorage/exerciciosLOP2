num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)
soma = num1 + num2 + num3
media = soma / 3

print(f"maior = {maior}")
print(f"menor = {menor}")
print(f"soma = {soma}")
print(f"media = {media}")
