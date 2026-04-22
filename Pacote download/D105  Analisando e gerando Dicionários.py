def notas(*n, sit=False):
    """
    → Função para avaliar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a turma.
    """
    nts = {}
    nts['total'] = len(n)
    nts['maior'] = max(n)
    nts['menor'] = min(n)
    nts['media'] = sum(n)/len(n)
    if sit:
        if nts['media'] >= 7:
            nts['situação'] = 'BOA'
        elif nts['media'] >= 5:
            nts['situação'] = 'RAZOÁVEL'
        else:
            nts['situação'] = 'RUIM'
    return nts



# Programa principal

resp = notas(5.5, 2, 10, 1.2, 4.5, sit=True)
print(resp)
help(notas)