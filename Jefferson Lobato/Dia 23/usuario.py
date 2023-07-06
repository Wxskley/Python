class Usuario:
    def __init__(self, primeiro_nome, ultimo_nome, idade, cidade, sexo):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.idade = idade
        self.cidade = cidade
        self.sexo = sexo

    def descricao_usuario(self):
        print(self.primeiro_nome.title() + " " + self.ultimo_nome.title())
        print(f"{int(self.idade)} anos.")
        print(f"Nascido em {self.cidade}")
        print(f"Do sexo {self.sexo}")

    def saudacao_usuario(self):
        print(
            f"Olá {self.primeiro_nome.title()} {self.ultimo_nome.title()} Seja bem vindo",
        )


usuario1 = Usuario("weskley", "dias", 21, "Mauriti", "Masculino")
usuario2 = Usuario("peba", "santos", 30, "brasilia", "Masculino")
usuario3 = Usuario("fulano", "amoeba", 52, "fortaleza", "Masculino")
usuario1.saudacao_usuario()
usuario1.descricao_usuario()
usuario2.saudacao_usuario()
usuario2.descricao_usuario()
usuario3.saudacao_usuario()
usuario3.descricao_usuario()
