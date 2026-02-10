# Lista de portas que quero verificar.
portas = [21, 22, 25, 80, 110, 443, 8080]

# Aqui eu tinha que usar apenas if, elif e else.
# No if eu coloquei as portas críticas (22 e 443).
# No elif ficaram as portas web (80 e 8080).
# E no else todo o resto virou comum.
# O resultado foi exatamente o que o ChatGPT me pediu.
for porta in portas:
    if porta == 22 or porta == 443:
        print(f"Porta {porta} -> CRÍTICA")
    elif porta == 80 or porta == 8080:
        print(f"Porta {porta} -> WEB")
    else:
        print(f"Porta {porta} -> COMUM")

