# Responsáveis por mostrar mensagem na tela de início do script.
print("Iniciando programa de ~PAR ou ÍMPAR~")
print("[PROGRAMA INICIADO COM SUCESSO]")

# O input faz a pergunta, o int transforma em número,
# e a variável 'limite' guarda o resultado.
limite = int(input("Até qual número devemos contar: "))

# O range gera uma sequência de números até o limite que o usuário digitou.
# O for repete o código pra cada número, mostrando se é PAR ou ÍMPAR.
for atual in range(limite + 1):
    if atual % 2 == 0:
        print(f"{atual} é PAR")
    else:
        print(f"{atual} é ÍMPAR")

# Foi aqui que descobri que o operador % 2 mostra o resto da divisão por 2.
# Se o resto for 0, o número é par. Se for 1, é ímpar.

