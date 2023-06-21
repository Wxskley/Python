from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
import pandas as pd


# Dados de exemplo
dataset = [
    ["Leite", "Cerveja", "Pão"],
    ["Leite", "Cerveja"],
    ["Leite", "Refrigerante", "Pão"],
    ["Leite", "Cerveja", "Refrigerante", "Pão"],
    ["Cerveja", "Refrigerante"],
]

# Codificando os dados de transação
te = TransactionEncoder()
te_ary = te.fit_transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Aplicando o algoritmo Apriori
frequent_itemsets = apriori(df, min_support=0.2, use_colnames=True)

# Exibindo os resultados
print(frequent_itemsets)
