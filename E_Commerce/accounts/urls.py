
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)
from .views import CustomObtainTokenPairView, AuthViewSets

app_name = "user"

# router = DefaultRouter()
# router.register("users", AuthViewSets)

urlpatterns = [
    # path("", include(router.urls)),
    path('login/', CustomObtainTokenPairView.as_view(), name='login'),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh-token"),
    path("token/verify/", TokenVerifyView.as_view(), name="verify-token"),
    # path('buyersignup', views.BuyerSignUpView.as_view(), name="buyersignup"),
    # path('vendorsignup', views.VendorSignUpView.as_view(), name="vendorsignup"),
    # path('buyerloginview/', views.BuyerLoginView.as_view(), name="buyerloginview"),
    # path('vendorloginview', views.VendorLoginView.as_view(), name='vendorloginview'),
    # path('jwt/create/', TokenObtainPairView.as_view(), name='jwt_create'),
    # path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify')
]
