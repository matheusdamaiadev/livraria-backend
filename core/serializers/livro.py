from rest_framework import serializers
from core.models import Livro
from uploader.models import Image


# =========================
# CREATE / UPDATE
# =========================
class LivroSerializer(serializers.ModelSerializer):
    capa = serializers.PrimaryKeyRelatedField(
        queryset=Image.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Livro
        fields = [
            'id',
            'titulo',
            'isbn',
            'quantidade',
            'preco',
            'categoria',
            'editora',
            'autores',
            'capa',
        ]

    def create(self, validated_data):
        autores = validated_data.pop('autores', [])

        livro = Livro.objects.create(**validated_data)

        if autores:
            livro.autores.set(autores)

        return livro

    def update(self, instance, validated_data):
        autores = validated_data.pop('autores', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        if autores is not None:
            instance.autores.set(autores)

        return instance


# =========================
# LISTAGEM SIMPLES
# =========================
class LivroListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Livro
        fields = (
            'id',
            'titulo',
            'preco',
            'categoria',
            'editora',
        )


# =========================
# DETALHE COMPLETO
# =========================
class LivroRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Livro
        fields = '__all__'