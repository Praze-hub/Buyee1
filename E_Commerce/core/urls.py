from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/v1/doc/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/v1/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("api/v1/api-auth/", include("rest_framework.urls")),
    path("admin/", admin.site.urls),
    # path("__debug__/", include("debug_toolbar.urls")),
    path('api/v1/product', include('product.urls.product_urls')),
    path('api/v1/brand', include('product.urls.brand_urls')),
    path('api/v1/category', include('product.urls.category_urls')),
]
