def notas(*notas, situacao=False):
    """
    Função para calcular informações sobre notas de alunos.
    :param notas: Notas dos alunos.
    :param situacao: Indica se a situação do aluno será exibida.
    :return: Dicionário com as informações sobre as notas.
    """
    info_notas = {
        "Quantidade de Notas": len(notas),
        "Maior Nota": max(notas),
        "Menor Nota": min(notas),
        "Média da Turma": sum(notas) / len(notas),
    }

    if situacao:
        if info_notas["Média da Turma"] >= 7:
            info_notas["Situação"] = "Aprovado"
        else:
            info_notas["Situação"] = "Reprovado"

    return info_notas


# Exemplo de uso da função
info = notas(8, 9.5, 7.2, 6.8, situacao=True)

# Exibição das informações das notas
for chave, valor in info.items():
    print(f"{chave}: {valor}")
