from django.conf.urls import include, url

urlpatterns = [
    url(r"^items/", include("items.urls")),
]
