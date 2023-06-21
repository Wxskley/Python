import pandas as pd
from mlxtend.frequent_patterns import fpgrowth

# Dados de exemplo
dataset = [
    ["Leite", "Cerveja", "Pão"],
    ["Leite", "Cerveja"],
    ["Leite", "Refrigerante", "Pão"],
    ["Leite", "Cerveja", "Refrigerante", "Pão"],
    ["Cerveja", "Refrigerante"],
]

# Convertendo a lista em DataFrame do Pandas
df = pd.DataFrame(dataset)

# Aplicando a codificação one-hot
df_encoded = pd.get_dummies(df.stack()).sum(level=0)

# Aplicando o algoritmo FP-Growth
frequent_itemsets = fpgrowth(df_encoded, min_support=0.2, use_colnames=True)

# Exibindo os resultados
print(frequent_itemsets)
