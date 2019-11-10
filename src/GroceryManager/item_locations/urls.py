from rest_framework import routers

from .views import ItemLocationViewSet

router = routers.SimpleRouter()
router.register(r"", ItemLocationViewSet)

urlpatterns = router.urls
