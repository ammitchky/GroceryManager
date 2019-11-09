import logging

from rest_framework import mixins, viewsets
from rest_framework.permissions import DjangoModelPermissions
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Item_Definition
from .serializers import Item_DefinitionSerializer

log = logging.getLogger(__name__)


class Item_DefinitionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = Item_DefinitionSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = Item_Definition.objects.all()
