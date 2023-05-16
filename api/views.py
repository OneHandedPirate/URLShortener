from rest_framework import viewsets, mixins

from .seralizers import TokenCreateSerializer
from urls.models import Token


class CreateListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = Token.objects.all().order_by('-created_at')
    serializer_class = TokenCreateSerializer
