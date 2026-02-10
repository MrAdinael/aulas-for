import time

print("===Iniciando Sistema de Verificação de Portas===")
time.sleep(1)

print("[SISTEMA INICIADO COM SUCESSO]")
time.sleep(1)

# Aqui eu comecei a deixar o range de lado e fui testar percorrer listas.
# Criei uma lista com portas abertas e fechadas.
portas = ["aberta", "fechada", "fechada", "aberta"]

# O for passa por cada item da lista e verifica se a porta está aberta ou fechada.
# Usei o time.sleep só pra dar um efeito visual, tipo uma pausa entre as mensagens.
for porta in portas:
    if porta == "aberta":
        print("[!] ALVO ENCONTRADO: Porta aberta!")
        time.sleep(0.2)
    elif porta == "fechada":
        print(".")
        time.sleep(0.2)

