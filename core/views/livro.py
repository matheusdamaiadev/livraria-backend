from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from core.models import Livro
from core.serializers import LivroSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    permission_classes = [permissions.AllowAny]
