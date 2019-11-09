from rest_framework import routers

from .views import Item_GroupViewSet

router = routers.SimpleRouter()
router.register(r"", Item_GroupViewSet)

urlpatterns = router.urls
