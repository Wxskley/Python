import asyncio  # Importa o módulo asyncio para suportar programação assíncrona.
import aiohttp  # Importa o módulo aiohttp para fazer requisições HTTP assíncronas.


# Define a função assíncrona fazer_requisicao para realizar uma requisição assíncrona a uma URL.
async def fazer_requisicao(url):
    # Cria uma sessão assíncrona de cliente HTTP.
    async with aiohttp.ClientSession() as session:
        # Envia uma requisição GET assíncrona à URL fornecida.
        async with session.get(url) as response:
            # Lê a resposta da requisição e converte para formato JSON.
            dados = await response.json()
            return dados  # Retorna os dados obtidos.


# Define a função assíncrona consultar_dados para realizar a consulta assíncrona aos dados.
async def consultar_dados():
    url = "https://api.exemplo.com/dados"  # URL para consulta dos dados.
    dados = await fazer_requisicao(
        url
    )  # Faz a requisição assíncrona e aguarda pelos dados.
    print("Dados:", dados)  # Imprime os dados obtidos.


loop = asyncio.get_event_loop()  # Obtém o loop de eventos assíncrono.
loop.run_until_complete(
    consultar_dados()
)  # Executa a função consultar_dados de forma assíncrona.
loop.close()  # Encerra o loop de eventos.
