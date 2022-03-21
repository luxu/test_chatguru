from requests import get
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import (
    PlanetasSerializer,
    PlanetaCriarSerializer,
    PlanetaAtualizarSerializer,
    FilmesSerializer,
    FilmeCriarSerializer,
    FilmeAtualizarSerializer,
    FilmesDoPlanetaSerializer
)
from backend.models import Planeta, Filme


@api_view(['GET'])
def planetas(request):
    planetas = Planeta.objects.all()
    serializer = PlanetasSerializer(planetas, many=True)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
def adicionar_planeta(request):
    serializer = PlanetaCriarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def atualizar_planeta(request, id):
    if id is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        planeta = Planeta.objects.get(id=id)
        serializer = PlanetaAtualizarSerializer(
            planeta, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Planeta.DoesNotExist:
        return Response(
            f"O planeta com ID:{id} não existe!",
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['DELETE'])
def deletar_planeta(request, id):
    if id is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        planeta = Planeta.objects.get(id=id)
        planeta.delete()
        return Response(
            f"O filme..: {planeta.nome} foi deletado com sucesso!",
            status=status.HTTP_204_NO_CONTENT
        )
    except Planeta.DoesNotExist:
        return Response(
            f"O planeta com ID:{id} não existe!",
            status=status.HTTP_404_NOT_FOUND
        )


# ------------------------------------ FILMES -------------------------------------
@api_view(['GET'])
def filmes(request):
    filmes = Filme.objects.all()
    serializer = FilmesSerializer(filmes, many=True)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
def adicionar_filme(request):
    serializer = FilmeCriarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def atualizar_filme(request, id):
    if id is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        filme = Filme.objects.get(id=id)
        serializer = FilmeAtualizarSerializer(
            filme, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Filme.DoesNotExist:
        return Response(
            f"O filme com ID:{id} não existe!",
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['DELETE'])
def deletar_filme(request, id):
    if id is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        filme = Filme.objects.get(id=id)
        filme.delete()
        return Response(
            f"O filme..: {filme.nome} foi deletado com sucesso!",
            status=status.HTTP_204_NO_CONTENT
        )
    except Filme.DoesNotExist:
        return Response(
            f"O filme com ID:{id} não existe!",
            status=status.HTTP_404_NOT_FOUND
        )


# ------------------------------------ FUNÇÕES -------------------------------------
@api_view(['GET'])
def films_do_planet(request, planeta_id):
    filmes = Filme.objects.filter(planetas=planeta_id)
    serializer = FilmesDoPlanetaSerializer(filmes, many=True)
    if len(serializer.data) > 0:
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    return Response(
        "Sem filmes para o planeta passado!!",
        status=status.HTTP_200_OK
    )


def dados_api(request):
    resp = get('https://swapi.dev/api/planets/')
    if resp.status_code != 200:
        return Response("Xiii, deu ruim na API", status=status.HTTP_204_NO_CONTENT)
    for planeta in resp.json()['results']:
        nome = planeta['name']
        diametro = planeta['diameter']
        clima = planeta['climate']
        try:
            populacao = int(planeta['population'])
        except Exception:
            populacao = 0
        filmes = planeta['films']
        planeta = Planeta(
            nome=nome,
            clima=clima,
            diametro=diametro,
            populacao=populacao
        )
        planeta.save()
        for url_filme in filmes:
            resp_filme = get(url_filme)
            filme = resp_filme.json()
            nome = filme['title']
            data_lancamento = filme['release_date']
            filme = Filme(
                nome=nome,
                data_lancamento=data_lancamento,
                planetas=planeta
            )
            filme.save()
    return Response("Dados salvos na base!", status=status.HTTP_201_CREATED)
