from django.urls import include, path
from rest_framework.routers import DefaultRouter
from ..views import (ProductView,)

app_name = "product"
router = DefaultRouter()

router.register("", ProductView)

urlpatterns = [
    path("", include(router.urls)),
]
