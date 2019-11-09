from django.conf.urls import include, url

urlpatterns = [
    url(r"^item/", include("items.urls")),
]