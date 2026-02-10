# Mensagem de início na tela.
print("====Iniciando sistema de aulafor====")
print("---sistema iniciado com sucesso---")

# Pergunta o nome e guarda na variável.
nome = input("Seu nome?: ")

# Pergunta a idade, transforma em número e guarda na variável.
idade = int(input("[DIGITE APENAS NUMEROS]~Sua idade?: "))

# Minha primeira vez usando range()!
# Aqui o for repete o resultado 5 vezes.
# Ele pega os dados que já foram guardados e mostra de novo.
for t in range(5):
    print("Seu nome é", nome, ", vc tem", idade, "anos")

