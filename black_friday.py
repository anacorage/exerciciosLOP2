preco = float(input("Digite o valor da compra: "))
print("Forma de pagamento:")
print("1 - À vista")
print("2 - Débito")
print("3 - Crédito")
print("4 - PIX")

opcao = int(input("Escolha: "))

if opcao == 1:
    desconto = 0.10
elif opcao == 2:
    desconto = 0.05
elif opcao == 3:
    desconto = 0.03
elif opcao == 4:
    desconto = 0.075
else:
    print("Opção inválida!")
    desconto = 0

valor_final = preco - (preco * desconto)
print(f"Valor final: R$ {valor_final:.2f}")
