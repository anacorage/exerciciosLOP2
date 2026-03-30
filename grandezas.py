print("******************************")
print("CÁLCULO DE GRANDEZAS ELÉTRICAS")
print("******************************")
print("1. Tensão (Volt)")
print("2. Resistência (Ohm)")
print("3. Corrente (Ampere)")
print("4. Sair")
print("******************************")

opcao = int(input("Qual grandeza deseja calcular? "))

if opcao == 1:
    R = float(input("Digite a resistência (Ohm): "))
    I = float(input("Digite a corrente (Ampere): "))
    U = R * I
    print(f"Tensão: {U} V")

elif opcao == 2:
    U = float(input("Digite a tensão (Volt): "))
    I = float(input("Digite a corrente (Ampere): "))
    R = U / I
    print(f"Resistência: {R} Ohm")

elif opcao == 3:
    U = float(input("Digite a tensão (Volt): "))
    R = float(input("Digite a resistência (Ohm): "))
    I = U / R
    print(f"Corrente: {I} A")

elif opcao == 4:
    print("Encerrando...")

else:
    print("Opção inválida!")
