import cv2
import numpy as np
from sklearn.svm import OneClassSVM

# Carregamento da imagem de exemplo
imagem = cv2.imread(
    r"ChatGPT\Dia 8\Machine Learning\Aprendizado não supervisionado\Algoritmos de detecção de anomalias\One-Class SVM\imagem.jpg",
    0,
)

# Reformatar os dados da imagem para um formato adequado
dados = imagem.reshape(-1, 1)

# Criação do modelo
modelo = OneClassSVM(nu=0.1)

# Treinamento do modelo
modelo.fit(dados)

# Detecção de anomalias
anomalias = modelo.predict(dados)

# Exibição dos resultados
imagem_anomalias = np.where(anomalias == -1, 255, imagem)
cv2.imshow("Imagem com Anomalias", imagem_anomalias)
cv2.waitKey(0)
cv2.destroyAllWindows()
