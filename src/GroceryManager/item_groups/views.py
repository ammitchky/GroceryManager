import logging

from rest_framework import mixins, viewsets
from rest_framework.permissions import DjangoModelPermissions
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Item_Group
from .serializers import Item_GroupSerializer

log = logging.getLogger(__name__)


class Item_GroupViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = Item_GroupSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = Item_Group.objects.all()
