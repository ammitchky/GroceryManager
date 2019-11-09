import logging

from rest_framework import mixins, viewsets
from rest_framework.permissions import DjangoModelPermissions
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Item
from .serializers import ItemSerializer

log = logging.getLogger(__name__)


class ItemsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = Item.objects.all()
