from django.conf.urls import include, url

urlpatterns = [
    url(r"^items/", include("items.urls")),
    url(r"^item_locations/", include("item_locations.urls")),
    url(r"^item_definitions/", include("item_definitions.urls")),
    url(r"^item_groups/", include("item_groups.urls")),
    url(r"^user_groups/", include("user_groups.urls")),
]
