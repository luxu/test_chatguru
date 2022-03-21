import json

from django.contrib.auth import get_user_model


def test_user_create(db):
    get_user_model().objects.create_user('foo@email.com', 'bar')
    assert get_user_model().objects.count() == 1


def test_listar_planetas(client, db):
    response = client.get('/api/v1/planetas/')
    resultado = json.loads(response.content)
    assert response.status_code == 200
    assert type(resultado) == list


def test_criar_planeta(client, db):
    payload = {
        "nome": "Lua",
        "clima": "frozen",
        "diametro": 7200,
        "populacao": 0
    }
    response = client.post(
        '/api/v1/planeta/adicionar_planeta/',
        data=payload,
        content_type='application/json'
    )
    resultado = json.loads(response.content)
    assert resultado['nome'] == 'Lua'


def test_tentar_atualizar_planeta_com_id_que_nao_existe(client, db):
    payload = {
        "nome": "Lua",
        "clima": "frozen",
        "diametro": 7200,
        "populacao": 0
    }
    url = 'http://127.0.0.1:8000/api/v1/planeta/atualizar_planeta/1/'
    response = client.put(url, data=payload)
    resultado = json.loads(response.content)
    assert resultado == "O planeta com ID:1 não existe!"


def test_atualizar_planeta_com_id_que_existe(planeta, client):
    payload = {"nome": "Lua"}
    url = f'http://127.0.0.1:8000/api/v1/planeta/atualizar_planeta/{planeta.id}/'
    response = client.put(url, data=payload, format='json', content_type="application/json")
    resultado = json.loads(response.content)
    assert resultado['nome'] == "Lua"


def test_tentar_deletar_planeta_com_id_que_nao_existe(planeta, client):
    url = 'http://127.0.0.1:8000/api/v1/planeta/deletar_planeta/12/'
    resultado = client.delete(url)
    assert resultado.data == "O planeta com ID:12 não existe!"


def test_tentar_deletar_planeta_com_id_que_existe(planeta, client):
    url = f'http://127.0.0.1:8000/api/v1/planeta/deletar_planeta/{planeta.id}/'
    resultado = client.delete(url)
    assert resultado.data == f'O filme..: {planeta.nome} foi deletado com sucesso!'


def test_listar_filmes(client, db):
    response = client.get('/api/v1/filmes/')
    resultado = json.loads(response.content)
    assert response.status_code == 200
    assert type(resultado) == list

def test_criar_filme(client, db, planeta):
    payload = {
        "nome": "Attack of the Clones",
        "data_lancamento": "2002-05-16T00:00:00-03:00",
        "planetas": planeta.id
    }
    response = client.post(
        '/api/v1/planeta/adicionar_filme/',
        data=payload
    )
    resultado = json.loads(response.content)
    assert resultado['nome'] == 'Attack of the Clones'


def test_atualizar_file_com_id_que_existe(filme, client):
    payload = {"nome": "Lua"}
    url = f'/api/v1/planeta/atualizar_filme/{filme.id}/'
    response = client.patch(url, data=payload, format='json', content_type="application/json")
    resultado = json.loads(response.content)
    assert resultado['nome'] == "Lua"

def test_deletar_filme(filme, client):
    url = f'http://127.0.0.1:8000/api/v1/planeta/deletar_filme/{filme.id}/'
    resultado = client.delete(url)
    assert resultado.data == f'O filme..: {filme.nome} foi deletado com sucesso!'

def test_nenhum_filme_do_planeta(client, db, planeta):
    url = f'/api/v1/filmes_do_planeta/{planeta.id}/'
    response = client.get(url)
    assert response.data == 'Sem filmes para o planeta passado!!'

def test_filmes_do_planeta(client, db, filme):
    url = f'/api/v1/filmes_do_planeta/{filme.planetas.id}/'
    response = client.get(url)
    assert response.data[0]['nome'] == 'Um passo para humanidade'
