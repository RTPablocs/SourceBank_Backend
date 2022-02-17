from django.urls import path
from .views import *

app_name = 'vaults'

urlpatterns = [
    path('new/', CreateVault.as_view()),
    path('update/', UpdateVault.as_view()),
    path('delete/', DropVault.as_view())
]
