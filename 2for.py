# Mensagem de início da script.
print("Iniciando sistema de for 2")
print("sistema iniciado")

# Pergunta, transforma em número e guarda.
numero = int(input("[APENAS NUMERO]~ Digite qual numero quer dividir por 2: "))

# Foi aqui que eu descobri que dava pra usar o range junto com operações.
# Tipo dividir, multiplicar, somar, subtrair, pegar resto etc.
# Nesse exemplo, o for repete 2 vezes a divisão por 2.
for t in range(2):
    print(f"Dividindo {numero} por 2...")
    print(numero / 2)

