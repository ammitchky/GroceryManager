from rest_framework import routers

from .views import Item_DefinitionViewSet

router = routers.SimpleRouter()
router.register(r"", Item_DefinitionViewSet)

urlpatterns = router.urls
