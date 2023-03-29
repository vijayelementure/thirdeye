from django.urls import path
from .views import login, reset

urlpatterns = [
    path("login/", login, name="login"),
    path("reset/", reset, name="reset"),
]
