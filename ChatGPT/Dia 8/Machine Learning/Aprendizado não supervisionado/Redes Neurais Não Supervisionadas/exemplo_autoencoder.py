import tensorflow as tf
from keras.layers import Input, Dense
from keras.models import Model

# Definindo a arquitetura do autoencoder
input_dim = 784  # Número de pixels da imagem MNIST
encoding_dim = 32  # Dimensão do código latente

input_img = Input(shape=(input_dim,))
encoded = Dense(encoding_dim, activation="relu")(input_img)
decoded = Dense(input_dim, activation="sigmoid")(encoded)

# Criando o modelo do autoencoder
autoencoder = Model(input_img, decoded)

# Compilando o modelo
autoencoder.compile(optimizer="adam", loss="binary_crossentropy")

# Carregar os dados de treinamento (por exemplo, imagens MNIST)
(X_train, _), (_, _) = tf.keras.datasets.mnist.load_data()

# Pré-processamento dos dados
X_train = X_train.reshape(-1, input_dim) / 255.0

# Treinando o autoencoder com os dados de treinamento
autoencoder.fit(X_train, X_train, epochs=10, batch_size=256, shuffle=True)
