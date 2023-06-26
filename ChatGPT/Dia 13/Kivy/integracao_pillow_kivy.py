from kivy.app import App
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
from PIL import Image as PILImage
from io import BytesIO


class MeuApp(App):
    def build(self):
        # Carrega a imagem usando o Pillow
        with open("ChatGPT\Dia 13\Kivy\imagem.png", "rb") as arquivo:
            imagem_bytes = arquivo.read()

        imagem_pillow = PILImage.open(BytesIO(imagem_bytes))

        # Redimensiona a imagem para uma largura de 300 pixels
        imagem_redimensionada = imagem_pillow.resize((300, 300))

        # Converte a imagem redimensionada para um formato suportado pelo Kivy
        imagem_bytes = BytesIO()
        imagem_redimensionada.save(imagem_bytes, format="png")
        imagem_bytes.seek(0)

        # Cria o widget de imagem do Kivy com a textura da imagem convertida
        texture = CoreImage(BytesIO(imagem_bytes.getvalue()), ext="png").texture
        image = Image(texture=texture)

        # Retorna o widget de imagem como raiz da interface gráfica
        return image


# Executa o aplicativo
if __name__ == "__main__":
    MeuApp().run()
