#fluxo de controle do python

user = input("Informe o nome de usuário: ")

if user in ("user1", "user2", "user3"):
    password = input("Digite sua senha: ")
    print("Login realizado com sucesso")
else:
    print("Usuário não existe")

