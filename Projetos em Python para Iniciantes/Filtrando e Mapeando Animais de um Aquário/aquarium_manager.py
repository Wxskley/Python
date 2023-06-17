import json

# Abre o arquivo JSON contendo os dados do aquário
f = open(
    r"Projetos em Python para Iniciantes\Filtrando e Mapeando Animais de um Aquário\aquarium.json",
    encoding="utf8",
)

# Carrega os dados do aquário a partir do arquivo JSON
data_aquarium = json.load(f)

# Obtém a lista de animais do aquário
animals = data_aquarium["data"]


# Função para verificar se um animal é um peixe
def verify_fish(animal):
    if animal["type"] == "fish":
        return True
    return False


# Filtra a lista de animais, mantendo apenas os peixes
animals_fish = list(filter(verify_fish, animals))
print(animals_fish)


# Função para obter o nome de um animal
def animal_name(animal):
    return animal["name"]


# Obtém a lista de nomes dos peixes utilizando a função animal_name
animals_fish_name = list(map(animal_name, animals_fish))
print(animals_fish_name)


# Função para atribuir um novo número de tanque aos animais selecionados
def assign_to_tank(animals, names_selected, new_tank_number):
    # Função interna para modificar o número de tanque de um animal
    def change_tank_number(animal):
        if animal["name"] in names_selected:
            animal["tank number"] = new_tank_number
        return animal

    # Aplica a função change_tank_number a cada animal na lista de animais
    return list(map(change_tank_number, animals))


# Atribui o novo número de tanque aos animais selecionados
new_aquarium = assign_to_tank(animals, animals_fish_name, 42)
print(new_aquarium)
