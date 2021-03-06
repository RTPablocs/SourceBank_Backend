from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt

app_name = 'users'

urlpatterns = [
    path('me/', RetrieveMyOwnData.as_view(), name='me'),
    path('register/', RegisterAPIView.as_view()),
    path('token/', jwt.TokenObtainPairView.as_view()),
    path('check/', jwt.TokenVerifyView.as_view()),
    path('refresh/', jwt.TokenRefreshView.as_view())
]
