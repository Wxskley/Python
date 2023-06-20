import asyncio


# Definição de uma corrotina
async def minha_corrotina():
    print("Corrotina iniciada")
    await asyncio.sleep(1)  # Simulando uma tarefa assíncrona de espera
    print("Corrotina finalizada")


# Criando e executando um loop de eventos assíncronos
loop = asyncio.get_event_loop()
loop.run_until_complete(minha_corrotina())
loop.close()
