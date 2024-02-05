from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from E_Commerce.product import views


router = DefaultRouter()
router.register(r"category", views.CategoryView)
router.register(r"brand", views.BrandView)
router.register(r"product", views.ProductView)




urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(api_version='v1'), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema', ), name ='swagger-ui'),
    path('api/auth/', include('E_Commerce.accounts.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)