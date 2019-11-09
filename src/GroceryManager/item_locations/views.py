import logging

from rest_framework import mixins, viewsets
from rest_framework.permissions import DjangoModelPermissions
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Item_Location
from .serializers import Item_LocationSerializer

log = logging.getLogger(__name__)


class Item_LocationViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = Item_LocationSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = Item_Location.objects.all()