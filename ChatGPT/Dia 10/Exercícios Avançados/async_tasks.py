# Vamos executar tarefas assíncronas usando async/await

import asyncio


# Vamos definir uma função assíncrona que simula uma tarefa demorada
async def long_running_task(name):
    print(f"Iniciando tarefa: {name}")
    await asyncio.sleep(2)  # Vamos pausar a execução por 2 segundos
    print(f"Tarefa concluída: {name}")


# Vamos criar uma função assíncrona para executar várias tarefas
async def run_tasks():
    # Vamos criar as tarefas
    task1 = asyncio.create_task(long_running_task("Tarefa 1"))
    task2 = asyncio.create_task(long_running_task("Tarefa 2"))

    # Vamos aguardar a conclusão de todas as tarefas
    await asyncio.gather(task1, task2)


# Vamos iniciar o loop de eventos para executar as tarefas
asyncio.run(run_tasks())
