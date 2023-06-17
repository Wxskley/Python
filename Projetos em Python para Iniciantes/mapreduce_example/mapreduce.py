import json
from functools import reduce

# Abre o arquivo JSON contendo os dados do aquário
f = open(
    r"Projetos em Python para Iniciantes\Filtrando e Mapeando Animais de um Aquário\aquarium.json",
    encoding="utf8",
)
data_aquarium = json.load(f)

# Extrai a lista de animais do aquário dos dados carregados
animals = data_aquarium["data"]


# Função para selecionar o tipo de animal e atribuir uma contagem inicial de 1
def pick_animal_type(animal):
    return animal["type"], 1


# Função de redução para contar o número de animais de cada tipo
def reducer(acc, val):
    # Verifica se o tipo de animal já existe no acumulador (acc)
    if val[0] not in acc.keys():
        # Se não existe, cria uma nova chave e atribui o valor 1
        acc[val[0]] = 0 + val[1]
    else:
        # Se já existe, incrementa o valor existente
        acc[val[0]] = acc[val[0]] + val[1]
    return acc


# Aplica a função pick_animal_type a cada animal da lista, obtendo uma lista de tuplas contendo o tipo de animal e a contagem inicial de 1
type_animals = list(map(pick_animal_type, animals))
print(type_animals)

# Utiliza a função reduce para aplicar a função reducer aos elementos da lista type_animals
# O valor inicial é um dicionário vazio ({}) que será utilizado como o valor inicial do acumulador (acc)
# A função reducer será aplicada a cada elemento da lista, contabilizando o número de animais de cada tipo
# O resultado final é um dicionário contendo o tipo de animal como chave e o número de ocorrências como valor
animals_type_count = reduce(reducer, type_animals, {})
print(animals_type_count)
