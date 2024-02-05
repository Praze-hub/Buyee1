from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (CategoryView, BrandView, ProductView,)

# app_name = "product"
router = DefaultRouter()

router.register("category", CategoryView)
router.register("brand", BrandView)
router.register("product", ProductView)

urlpatterns = [
    path("", include(router.urls)),
]