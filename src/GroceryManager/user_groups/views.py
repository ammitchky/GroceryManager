import logging

from rest_framework import mixins, viewsets
from rest_framework.permissions import DjangoModelPermissions
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import UserGroup
from .serializers import UserGroupSerializer

log = logging.getLogger(__name__)


class UserGroupViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = UserGroupSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = UserGroup.objects.all()
