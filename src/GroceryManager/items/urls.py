from rest_framework import routers

from .views import ItemsViewSet

router = routers.SimpleRouter()
router.register(r"", ItemsViewSet)

urlpatterns = router.urls
