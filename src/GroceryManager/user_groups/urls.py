from rest_framework import routers

from .views import User_GroupViewSet

router = routers.SimpleRouter()
router.register(r"", User_GroupViewSet)

urlpatterns = router.urls
