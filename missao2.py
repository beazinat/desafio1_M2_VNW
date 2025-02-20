def verificar_voto():
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade >= 0:
                return "Pode votar" if idade >= 16 else "Não pode votar"
            else:
                print("Idade inválida! Digite um valor positivo.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

print(verificar_voto())