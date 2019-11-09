from rest_framework import routers

from .views import Item_LocationViewSet

router = routers.SimpleRouter()
router.register(r"", Item_LocationViewSet)

urlpatterns = router.urls
