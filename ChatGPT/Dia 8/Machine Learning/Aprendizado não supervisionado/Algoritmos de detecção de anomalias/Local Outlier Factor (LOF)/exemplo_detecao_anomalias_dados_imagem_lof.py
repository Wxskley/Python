import cv2
import numpy as np
from sklearn.neighbors import LocalOutlierFactor

# Carregamento da imagem de exemplo
imagem = cv2.imread(
    r"C:\Users\Weskley\Documents\Programação\Python\ChatGPT\Dia 8\Machine Learning\Aprendizado não supervisionado\Algoritmos de detecção de anomalias\Local Outlier Factor (LOF)\imagem.jpg",
    0,
)

# Reformatar os dados da imagem para um formato adequado
dados = imagem.reshape(-1, 1)

# Criação do modelo
modelo = LocalOutlierFactor(contamination=0.1)

# Detecção de anomalias
anomalias = modelo.fit_predict(dados)

# Exibição dos resultados
imagem_anomalias = np.where(anomalias == -1, 255, imagem)
cv2.imshow("Imagem com Anomalias", imagem_anomalias)
cv2.waitKey(0)
cv2.destroyAllWindows()
