print("Iniciando programa")
print("concluido")

portas = [21, 22, 25, 80, 443]

# Aqui fiz o [for] percorrer por uma lista [portas] e mostrar qual é segura e qual é comum

for t in portas:
    if t == 22 or t == 443:
        print(f"[!] Porta: [{t}] é segura!")
    else:
        print(f"[-] Porta: [{t}] é comum!")

# Foi aqui que eu percebi que o for não serve só pra range().
# Ele também percorre coleções diferentes, tipo listas, strings e dicionários.
# No caso, estou usando uma lista chamada 'portas'.

