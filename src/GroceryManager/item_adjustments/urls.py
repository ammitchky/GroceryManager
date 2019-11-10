from rest_framework import routers

from .views import ItemAdjustmentViewSet

router = routers.SimpleRouter()
router.register(r"", ItemAdjustmentViewSet)

urlpatterns = router.urls
