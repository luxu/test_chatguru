import pytest

from backend.models import Planeta, Filme
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model

@pytest.fixture
def planeta(db):
    return Planeta.objects.create(
        nome="Saturno",
        clima="Nebuloso",
        diametro=1233221,
        populacao=1000000000
    )

@pytest.fixture
def filme(db, planeta):
    return Filme.objects.create(
        nome="Um passo para humanidade",
        data_lancamento="1983-11-23",
        planetas=planeta
    )

planets = [
        [Planeta(nome='Kamino', clima="temperate", diametro=19720, populacao=1000000000)],
        [Planeta(nome='Coruscant', clima='temperate', diametro=12240, populacao=1000000000)],
        [Planeta(nome='Naboo', clima='temperate', diametro=12120, populacao=4500000000)],
        [Planeta(nome='Endor', clima='temperate', diametro=4900, populacao=30000000)],
        [Planeta(nome='Bespin', clima='temperate', diametro=118000, populacao=6000000)],
        [Planeta(nome='Dagobah', clima='murky', diametro=8900, populacao=0)]
    ]
@pytest.fixture(params=planets)
def planetas(request):
    return request.param


@pytest.fixture
def create_user(db):
    email = 'foo@email.com'
    password = 'bar'
    return get_user_model().objects.create_user(email=email, password=password)

@pytest.fixture
def api_client(create_user):
    token = Token.objects.create(user=create_user)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
    return client
