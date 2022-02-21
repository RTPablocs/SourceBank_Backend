from django.urls import path
from .views import *
from vaults.views import ListVaultMovements

app_name = 'movements'

urlpatterns = [
    path('transaction/', RegisterMovement.as_view(), name='transaction'),
    path('vault/', RegisterVaultMovement.as_view()),
    path('vault/<vault_id>', ListVaultMovements.as_view())
]
