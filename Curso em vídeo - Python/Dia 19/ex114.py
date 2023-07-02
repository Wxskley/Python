import requests

url = "http://www.pudim.com.br"

try:
    response = requests.get(url)
    response.raise_for_status()  # Verifica se ocorreu algum erro na requisição

    print("O site pudim está acessível.")
except requests.HTTPError:
    print("O site pudim está inacessível.")
except requests.RequestException:
    print("Não foi possível conectar ao site pudim.")
