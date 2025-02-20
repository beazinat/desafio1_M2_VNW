def classificar_nota():
    while True:
        try:
            nota = float(input("Digite a nota do aluno (0 a 100): "))
            if 0 <= nota <= 100:
                if nota >= 90:
                    return "Parabéns, você tirou A!"
                elif nota >= 80:
                    return "Muito bem, você tirou B."
                elif nota >= 70:
                    return "Bom trabalho, você tirou C."
                elif nota >= 60:
                    return "Fique atento, você tirou D."
                else:
                    return "Estude um pouco mais, você tirou F."
            else:
                print("Nota inválida! Digite um valor entre 0 e 100.")
        except ValueError:
            print("Entrada inválida! Digite um número.")

print(classificar_nota())