import logging

from rest_framework import mixins, viewsets
from rest_framework.permissions import DjangoModelPermissions
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import ItemAdjustment
from .serializers import ItemAdjustmentSerializer

log = logging.getLogger(__name__)


class ItemAdjustmentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ItemAdjustmentSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = ItemAdjustment.objects.all()
