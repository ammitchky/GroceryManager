from rest_framework import routers

from .views import ItemGroupViewSet

router = routers.SimpleRouter()
router.register(r"", ItemGroupViewSet)

urlpatterns = router.urls
