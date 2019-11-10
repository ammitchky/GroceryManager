from rest_framework_extensions.routers import ExtendedSimpleRouter

from .views import ItemDefinitionViewSet, ItemSpecificationViewSet

router = ExtendedSimpleRouter()
services_router = router.register(
    r"", ItemDefinitionViewSet, basename="item_definitions"
)
services_router.register(
    r"specifications",
    ItemSpecificationViewSet,
    basename="specifications",
    parents_query_lookups=["definition"],
)

urlpatterns = router.urls
