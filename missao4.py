def somar_numeros():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            return f"A soma de {num1} e {num2} é {num1 + num2}"
        except ValueError:
            print("Entrada inválida! Digite números válidos.")

print(somar_numeros())