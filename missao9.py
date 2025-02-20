def dobro():
    while True:
        try:
            numero = float(input("Digite um número: "))
            return f"O dobro de {numero} é {numero * 2}"
        except ValueError:
            print("Entrada inválida! Digite um número.")

print(dobro())