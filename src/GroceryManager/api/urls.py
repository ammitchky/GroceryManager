from django.conf.urls import include, url

urlpatterns = [
    url(r"^items/", include("items.urls")),
    url(r"^item_locations/", include("item_locations.urls")),
]
