velocidade = float(input("Digite a velocidade em Km/h: "))

if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 50
    print(f"Limite = 80 Km/h")
    print(f"Excedeu {excesso} Km/h")
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    print("Velocidade dentro do limite.")
