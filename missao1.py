def verificar_aprovacao():
    while True:
        try:
            nota = float(input("Digite a nota do aluno (0 a 10): "))
            if 0 <= nota <= 10:
                return "Aprovado" if nota >= 6 else "Reprovado"
            else:
                print("Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite um número.")

print(verificar_aprovacao())