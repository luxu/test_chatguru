from rest_framework import serializers

from backend.models import Planeta, Filme


class PlanetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planeta
        fields = (
            'id',
            'nome',
            "clima",
            "diametro",
            "populacao"
        )


class PlanetaCriarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planeta
        fields = (
            "nome",
            "clima",
            "diametro",
            "populacao"
        )


class PlanetaAtualizarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planeta
        fields = (
            "nome",
            "clima",
            "diametro",
            "populacao"
        )


# --------------------------------------- FILMES ----------------------------
class FilmesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = (
            'id',
            'nome',
            'data_lancamento',
            'planetas',
        )


class FilmeCriarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = (
            'nome',
            'data_lancamento',
            'planetas',
        )

class FilmeAtualizarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = (
            'id',
            'nome',
            'data_lancamento',
            'planetas',
        )


class FilmesDoPlanetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = (
            'nome',
            'data_lancamento',
            'planetas',
        )
