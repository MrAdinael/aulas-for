print("Iniciando programa")
print("Concluido")

# Pergunta um número e guarda na variável.
num = int(input("Digite um número: "))

# Aqui eu configurei o range pra começar a sequência em 0
# e ir até o número que o usuário digitou.
# O for vai passar por cada número e mostrar só os pares.
for t in range(num + 1):
    if t % 2 == 0:
        print(f"O número: {t} é PAR")

