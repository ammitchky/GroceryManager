import logging

from rest_framework import mixins, viewsets
from rest_framework.permissions import DjangoModelPermissions
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import ItemLocation
from .serializers import ItemLocationSerializer

log = logging.getLogger(__name__)


class ItemLocationViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ItemLocationSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = ItemLocation.objects.all()
