import logging

from rest_framework import mixins, viewsets
from rest_framework.permissions import DjangoModelPermissions
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import ItemGroup
from .serializers import ItemGroupSerializer

log = logging.getLogger(__name__)


class ItemGroupViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ItemGroupSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = ItemGroup.objects.all()
