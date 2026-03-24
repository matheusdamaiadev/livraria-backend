from rest_framework.viewsets import ModelViewSet

from core.models import Livro
from core.serializers import LivroListSerializer, LivroRetrieveSerializer, LivroSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer  # padrão para criação/atualização

    def get_serializer_class(self):
        if self.action == 'list':
            return LivroListSerializer  # listagem simplificada
        elif self.action == 'retrieve':
            return LivroRetrieveSerializer  # detalhes de um livro
        return LivroSerializer  # criação/alteração
