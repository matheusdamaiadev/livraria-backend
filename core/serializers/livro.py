from rest_framework.serializers import ModelSerializer

from core.models import Livro


# Serializador para criação e atualização (POST, PUT, PATCH)
class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'


# Serializador para recuperação de um único livro com detalhes
class LivroRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
        depth = 1  # Exibe informações relacionadas de Categoria, Editora e Autores


# Serializador para listagem de livros (GET /api/livros/) com apenas campos essenciais
class LivroListSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = ('id', 'titulo', 'preco')
