from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('', views.Home, name='home'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('protected/', views.MyProtectedRoute, name='my_protected_route'),
    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]