class Restaurante:
    """Representa um restaurante"""

    def __init__(self, restaurante_nome, tipo_cozinha):
        self.restaurante_nome = restaurante_nome
        self.tipo_cozinha = tipo_cozinha

    def restaurante_descricao(self):
        print(
            f"O restaurante se chama {self.restaurante_nome} e sua especialidade é {self.tipo_cozinha}"
        )

    def restaurante_aberto(self):
        print(f"O restaurante {self.restaurante_nome} está aberto no momento!")


restaurante1 = Restaurante("Lá casa do pastel", "Pastelaria")
restaurante2 = Restaurante("Comida à Mineira", "Comida Mineira")
restaurante3 = Restaurante("Massa Fera", "Massas")
restaurante1.restaurante_descricao()
restaurante2.restaurante_descricao()
restaurante3.restaurante_descricao()
