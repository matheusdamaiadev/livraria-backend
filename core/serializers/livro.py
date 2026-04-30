from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from core.models import Livro
from uploader.models import Image


# =========================
# CREATE / UPDATE
# =========================
class LivroSerializer(ModelSerializer):
    capa = PrimaryKeyRelatedField(
        queryset=Image.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Livro
        fields = ('id', 'titulo', 'preco', 'categoria', 'editora', 'capa', 'autores')

    def update(self, instance, validated_data):
        # remove ManyToMany para tratar separadamente
        autores = validated_data.pop('autores', None)

        # atualiza campos normais
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        # atualiza ManyToMany corretamente
        if autores is not None:
            instance.autores.set(autores)

        return instance


# =========================
# RETRIEVE (DETALHADO)
# =========================
class LivroRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
        depth = 1  # categorias, editora, autores com detalhes


# =========================
# LISTAGEM SIMPLES
# =========================
class LivroListSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = (
            'id',
            'titulo',
            'preco',
            'capa',
            'categoria',
            'editora',
        )
