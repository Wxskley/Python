import asyncio


# Definição de uma corrotina chamada "tarefa"
async def tarefa(nome):
    print(f"Iniciando a tarefa {nome}")
    await asyncio.sleep(1)
    print(f"Tarefa {nome} concluída")


# Definição de uma corrotina chamada "executar_tarefas"
async def executar_tarefas():
    tarefas = [tarefa("A"), tarefa("B"), tarefa("C")]
    await asyncio.gather(*tarefas)


# Criando e executando um loop de eventos assíncronos
loop = asyncio.get_event_loop()
loop.run_until_complete(executar_tarefas())
loop.close()
