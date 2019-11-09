import logging

from rest_framework import mixins, viewsets
from rest_framework.permissions import DjangoModelPermissions
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import User_Group
from .serializers import User_GroupSerializer

log = logging.getLogger(__name__)


class User_GroupViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = User_GroupSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = User_Group.objects.all()
