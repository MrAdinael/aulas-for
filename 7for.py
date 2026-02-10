print("Iniciando programa")
print("concluido com sucesso")

# Criei uma lista com alguns números.
numeros = [3, 7, 10, 15, 18]

# Dessa vez eu usei o for direto na lista, sem range.
# Ele vai passar por cada número e mostrar se é múltiplo de 3 ou não.
for t in numeros:
    if t % 3 == 0:
        print(f"[!] O número: [{t}] é múltiplo de 3.")
    else:
        print(f"[-] O número: [{t}] não é múltiplo de 3.")

