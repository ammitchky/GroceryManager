import logging

from rest_framework import mixins, viewsets
from rest_framework.permissions import DjangoModelPermissions
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Item, ItemAdjustment
from .serializers import ItemSerializer, ItemAdjustmentSerializer
from rest_framework.decorators import action

log = logging.getLogger(__name__)


class ItemViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = Item.objects.all()

    @action(detail=True, methods=["post"])
    def adjust(self, request, pk):
        item = self.get_object()
        serializer = AdjustItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return ItemSerializer(item).data


class ItemAdjustmentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ItemAdjustmentSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = ItemAdjustment.objects.all()
