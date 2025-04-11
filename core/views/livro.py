from rest_framework.viewsets import ModelViewSet

from core.models import Autor
from core.serializers.autor import AutorSerializer


class LivroViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer