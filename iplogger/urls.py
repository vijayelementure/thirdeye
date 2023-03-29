from django.urls import path
from .views import dashboard, connectednode


urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("cnode/", connectednode, name="cnode"),
]
