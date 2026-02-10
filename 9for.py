# Lista de portas que quero verificar.
portas = [21, 22, 25, 80, 110, 443, 8080]

# Aqui eu quis fazer um filtro usando if.
# Na época eu nem sabia o que era "filtro", só lembrei que dava pra usar vários 'or'
# dentro do if pra escolher quais portas seriam aceitas.
# O resultado foi exatamente o que o ChatGPT me pediu: mostrar só as portas aceitas
# e não imprimir nada das outras.
for porta in portas:
    if porta == 22 or porta == 80 or porta == 443 or porta == 8080:
        print(f"Porta {porta} aceita!")

