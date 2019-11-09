import logging

from rest_framework import mixins, viewsets
from rest_framework.permissions import DjangoModelPermissions
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Item_Adjustment
from .serializers import Item_AdjustmentSerializer

log = logging.getLogger(__name__)


class Item_AdjustmentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = Item_AdjustmentSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = Item_Adjustment.objects.all()
