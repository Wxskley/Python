import requests


def obter_informacoes_repositorio(usuario, repositorio):
    # Defina a URL da API do GitHub para obter informações do repositório
    url = f"https://api.github.com/repos/{usuario}/{repositorio}"

    # Faça uma requisição GET para a API
    response = requests.get(url)

    # Verifique se a requisição foi bem-sucedida (código 200)
    if response.status_code == 200:
        # Obtenha os dados da resposta em formato JSON
        dados = response.json()

        # Extraia as informações relevantes do repositório
        nome = dados["name"]
        descricao = dados["description"]
        estrelas = dados["stargazers_count"]
        forks = dados["forks_count"]

        # Retorne os dados do repositório
        return {
            "nome": nome,
            "descricao": descricao,
            "estrelas": estrelas,
            "forks": forks,
        }
    else:
        # Caso a requisição falhe, retorne None
        return None


# Exemplo de uso da função para obter informações de um repositório do GitHub
usuario = "wxskley"
repositorio = "Python"

informacoes = obter_informacoes_repositorio(usuario, repositorio)

if informacoes:
    print(f"Informações do repositório {usuario}/{repositorio}:")
    print(f"Nome: {informacoes['nome']}")
    print(f"Descrição: {informacoes['descricao']}")
    print(f"Estrelas: {informacoes['estrelas']}")
    print(f"Forks: {informacoes['forks']}")
else:
    print("Não foi possível obter as informações do repositório.")
