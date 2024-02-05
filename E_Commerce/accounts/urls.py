
from django.urls import path
from . import views
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('register/',views.RegisterView.as_view(), name='register'),
    path('login/',views.LoginView.as_view(), name='login'),
    # path('buyersignup', views.BuyerSignUpView.as_view(), name="buyersignup"),
    # path('vendorsignup', views.VendorSignUpView.as_view(), name="vendorsignup"),
    # path('buyerloginview/', views.BuyerLoginView.as_view(), name="buyerloginview"),
    # path('vendorloginview', views.VendorLoginView.as_view(), name='vendorloginview'),
    # path('jwt/create/', TokenObtainPairView.as_view(), name='jwt_create'),
    # path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify')
]