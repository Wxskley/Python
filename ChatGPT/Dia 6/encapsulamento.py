# Definição da classe "ContaBancaria"
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado que armazena o saldo inicial da conta

    def depositar(self, valor):
        self.__saldo += valor  # Adiciona o valor informado ao saldo da conta

    def sacar(self, valor):
        if self.__saldo >= valor:  # Verifica se o saldo é suficiente para o saque
            self.__saldo -= valor  # Subtrai o valor do saldo
        else:
            print(
                "Saldo insuficiente."
            )  # Exibe mensagem de saldo insuficiente se não for possível sacar o valor

    def consultar_saldo(self):
        return self.__saldo  # Retorna o valor do saldo da conta


# Criação de um objeto da classe "ContaBancaria"
conta = ContaBancaria(1000)  # Cria uma nova conta bancária com saldo inicial de 1000

# Acesso aos atributos e chamada dos métodos do objeto
print("Saldo inicial:", conta.consultar_saldo())  # Exibe o saldo inicial da conta

conta.depositar(500)  # Deposita 500 na conta
print("Saldo após depósito:", conta.consultar_saldo())  # Exibe o saldo após o depósito

conta.sacar(200)  # Realiza um saque de 200
print("Saldo após saque:", conta.consultar_saldo())  # Exibe o saldo após o saque
