tipo = input("Tipo de combustível (A - Álcool, G - Gasolina): ").upper()
litros = float(input("Quantidade de litros: "))

if tipo == "A":
    preco_litro = 2.89
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05

elif tipo == "G":
    preco_litro = 4.95
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06

else:
    print("Tipo inválido")
    desconto = 0
    preco_litro = 0

total = litros * preco_litro
valor_final = total - (total * desconto)

print(f"Valor a pagar: R$ {valor_final:.2f}")
