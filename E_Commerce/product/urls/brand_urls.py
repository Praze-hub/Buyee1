from django.urls import include, path
from rest_framework.routers import DefaultRouter
from ..views import (CategoryView, BrandView, ProductView,)

app_name = "brand"
router = DefaultRouter()

router.register("", BrandView)

urlpatterns = [
    path("", include(router.urls)),
]