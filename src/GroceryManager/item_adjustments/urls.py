from rest_framework import routers

from .views import Item_AdjustmentViewSet

router = routers.SimpleRouter()
router.register(r"", Item_AdjustmentViewSet)

urlpatterns = router.urls
