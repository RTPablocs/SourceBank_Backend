from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt

app_name = 'users'

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('token/', jwt.TokenObtainPairView.as_view()),
    path('check/', jwt.TokenVerifyView.as_view()),
    path('<str:id>/', GetOrUpdateOwnData.as_view())
]