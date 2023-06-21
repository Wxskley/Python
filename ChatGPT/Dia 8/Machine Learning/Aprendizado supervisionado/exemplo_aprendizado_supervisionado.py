from sklearn import datasets  # Importando o módulo de conjuntos de dados
from sklearn.model_selection import (
    train_test_split,
)  # Importando a função de divisão de dados
from sklearn.neighbors import KNeighborsClassifier  # Importando o classificador KNN
from sklearn.metrics import accuracy_score  # Importando a métrica de acurácia

# Carregar o conjunto de dados de exemplo (conjunto de dados das flores Iris)
iris = datasets.load_iris()

# Separar os recursos (X) e os rótulos (y) do conjunto de dados
X = iris.data  # Recursos (comprimento e largura das pétalas e sépalas)
y = iris.target  # Rótulos (espécies de flores)

# Dividir o conjunto de dados em treinamento e teste usando a função train_test_split
# O parâmetro test_size define a proporção do conjunto de teste (20% neste caso)
# O parâmetro random_state garante a reproducibilidade dos resultados
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Criar um objeto classificador KNN
knn = KNeighborsClassifier()

# Treinar o modelo de classificação usando o conjunto de treinamento
knn.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = knn.predict(X_test)

# Calcular a acurácia do modelo comparando as previsões (y_pred) com os rótulos verdadeiros (y_test)
accuracy = accuracy_score(y_test, y_pred)

# Imprimir a acurácia do modelo
print(f"Acurácia: {accuracy}")
