# Faça uma função notas() que pode receber várias notas de alunos e retorne um dicionário com as seguintes informações:
# Quantidade de notas | A maior nota | A menor nota | A média da turma | A situação (opcional) | Add docstrings


def notas(*notas, situação=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias).
    :param situação: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = {'total': len(notas), 'maior': max(notas), 'menor': min(notas), 'média': sum(notas) / len(notas)}
    # r['total'] = len(notas)
    # r['maior'] = max(notas)
    # r['menor'] = min(notas)
    # r['média'] = sum(notas)/len(notas)
    if situação:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa principal
resp = notas(5.5, 2.5, 9, 8.5, situação=True)
print(resp)
help(notas)
