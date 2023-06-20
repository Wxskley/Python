import pandas as pd

# Dados de exemplo
dados = {
    "Nome": ["João", "Maria", "Pedro", "Ana"],
    "Idade": [25, 30, 20, 35],
    "Salário": [2500, 3500, 2000, 4000],
}

# Criação do DataFrame
df = pd.DataFrame(dados)

# Estatísticas básicas
print("Média das idades:", df["Idade"].mean())
print("Máximo salário:", df["Salário"].max())
print("Mínimo salário:", df["Salário"].min())
