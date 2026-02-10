print("Iniciando programa")
print("Concluido")

# Criei uma lista com alguns IPs.
ips = ["192.168.0.1", "10.0.0.5", "8.8.8.8"]

# Aqui eu voltei pra algo mais simples:
# se o IP for 8.8.8.8 ele é externo,
# se não for, cai no else e vira interno.
for ip in ips:
    if ip == "8.8.8.8":
        print(f"[EXTERNO] IP: {ip}")
    else:
        print(f"[INTERNO] IP: {ip}")

