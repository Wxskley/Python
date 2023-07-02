from utilidadesCeV.dado.dinheiro import leiaDinheiro
from utilidadesCeV.moeda.moeda import resumo

valor = leiaDinheiro("Digite um valor monetário: ")
print(f"O valor digitado foi: {valor}")
resumo(valor, 35, 22)
