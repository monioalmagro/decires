# Third-party Libraries
from django.urls import path, include

app_name = "core"

urlpatterns = [
    path("zona-usuario/", include("apps.core.urls.user"), name="user"),
]
