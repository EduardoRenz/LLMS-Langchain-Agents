

import pandas as pd


def get_aluno(name):
    dados = pd.read_csv("data/alunos.csv")
    dados_com_esse_estudante = dados[dados["nome"].str.lower() == name]
    if dados_com_esse_estudante.empty:
        return {}
    return dados_com_esse_estudante.iloc[:1].to_dict()
# aluno = get_aluno("pedro")
# print(aluno)
