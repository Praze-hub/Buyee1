from django.urls import include, path
from rest_framework.routers import DefaultRouter
from ..views import (CategoryView, BrandView, ProductView,)

app_name = "category"
router = DefaultRouter()

router.register("", CategoryView)

urlpatterns = [
    path("", include(router.urls)),
]