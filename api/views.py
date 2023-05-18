from rest_framework import viewsets, mixins

from .seralizers import TokenSerializer
from urls.models import Token


class CreateListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """Create token or return list of tokens"""

    queryset = Token.objects.all().order_by('-created_at')
    serializer_class = TokenSerializer
