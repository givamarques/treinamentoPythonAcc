nome = input("informe seu nome: ")
sobrenome = input("informe seu sobrenome: ")
nascimento = input("informe o ano de seu nascimento: ")

idade:int = 2023 - int(nascimento)

print(f"Você se chama: {nome} {sobrenome} e tem {idade} anos")
#f-string format permite "embedar" as variaveis mesmo de tipos diferentes no print