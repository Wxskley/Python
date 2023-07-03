import re

texto = "Curso de Python do CFB Cursos, canal do Youtube"
pesq = input("Pesquisar: ")
res = re.findall(pesq, texto)
print(res)
qtde = len(res)
print(f"Quantidade: {qtde}")
for t in res:
    print(t)
