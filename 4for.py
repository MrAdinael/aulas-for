print("Iniciando programa")
print("concluido")

# Pergunta o número inicial e guarda na variável.
num1 = int(input("Digite um número de início: "))

# Pergunta o número final e guarda na variável.
num2 = int(input("Digite um número final: "))

# Aqui eu configurei o range pra começar a sequência no número que o usuário pediu
# e parar no número final. O for vai passar por cada número e mostrar
# se ele é múltiplo de 3 ou não.
for t in range(num1, num2 + 1):
    if t % 3 == 0:
        print(f"{t} é múltiplo de 3")
    else:
        print(f"{t} não é múltiplo de 3")

# Foi aqui que percebi que dá pra usar o % (resto da divisão)
# pra descobrir se um número é múltiplo de outro.

