from rest_framework import routers

from .views import UserGroupViewSet

router = routers.SimpleRouter()
router.register(r"", UserGroupViewSet)

urlpatterns = router.urls
