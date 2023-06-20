import requests


def obter_previsao_tempo(cidade):
    # Defina a URL da API de previsão do tempo
    url = f"http://api.weatherapi.com/v1/current.json?key=SUA_CHAVE_API&q={cidade}"

    # Faça uma requisição GET para a API
    response = requests.get(url)

    # Verifique se a requisição foi bem-sucedida (código 200)
    if response.status_code == 200:
        # Obtenha os dados da resposta em formato JSON
        dados = response.json()

        # Extraia as informações relevantes da previsão do tempo
        temperatura = dados["current"]["temp_c"]
        umidade = dados["current"]["humidity"]
        descricao = dados["current"]["condition"]["text"]

        # Retorne os dados da previsão do tempo
        return {"temperatura": temperatura, "umidade": umidade, "descricao": descricao}
    else:
        # Caso a requisição falhe, retorne None
        return None


# Exemplo de uso da função para obter a previsão do tempo de uma cidade
cidade = input("Digite o nome da cidade: ")
previsao = obter_previsao_tempo(cidade)

if previsao:
    print(f"Previsão do tempo para {cidade}:")
    print(f"Temperatura: {previsao['temperatura']}°C")
    print(f"Umidade: {previsao['umidade']}%")
    print(f"Descrição: {previsao['descricao']}")
else:
    print("Não foi possível obter a previsão do tempo.")
