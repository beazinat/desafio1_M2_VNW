def verificar_senha():
    senha = input("Digite a senha: ")
    return "Senha correta! Acesso permitido." if senha == "Python123" else "Senha incorreta! Acesso negado."

print(verificar_senha())