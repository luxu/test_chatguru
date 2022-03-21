def test_retornar_nome_planeta(planeta):
    assert planeta.nome == 'Saturno'


def test_retornar_clima_planeta(planeta):
    assert planeta.clima == 'Nebuloso'


def test_retornar_diametro_planeta(planeta):
    assert planeta.diametro == 1233221


def test_retornar_populacao_planeta(planeta):
    assert planeta.populacao == 1000000000


def test_retornar_nome_filme(filme):
    assert filme.nome == 'Um passo para humanidade'


def test_retornar_data_lancamento_filme(filme):
    assert filme.data_lancamento == '1983-11-23'


def test_retornar_nome_planeta_filme(filme):
    assert filme.planetas.nome == "Saturno"
