import time

# Loop for para percorrer de 10 até 0
for contagem_regressiva in range(10, -1, -1):
    # Imprimir o número da contagem regressiva na tela
    print(contagem_regressiva)

    # Aguardar 1 segundo antes de imprimir o próximo número
    time.sleep(1)

# Imprimir a mensagem de estouro de fogos de artifício
print("Estouro de fogos de artifício!")
