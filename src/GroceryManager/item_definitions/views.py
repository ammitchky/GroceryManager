import logging

from rest_framework import mixins, viewsets
from rest_framework.permissions import DjangoModelPermissions
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import ItemDefinition, ItemSpecification
from .serializers import ItemDefinitionSerializer, ItemSpecificationSerializer

log = logging.getLogger(__name__)


class ItemDefinitionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ItemDefinitionSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = ItemDefinition.objects.all()


class ItemSpecificationViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ItemSpecificationSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = ItemSpecification.objects.all()
