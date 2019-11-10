from rest_framework_extensions.routers import ExtendedSimpleRouter

from .views import ItemViewSet, ItemAdjustmentViewSet

router = ExtendedSimpleRouter()
services_router = router.register(r"", ItemViewSet, basename="items")
services_router.register(
    r"adjustments",
    ItemAdjustmentViewSet,
    basename="adjustments",
    parents_query_lookups=["item"],
)

urlpatterns = router.urls
