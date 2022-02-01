from django.urls import path
from .views import *

app_name = 'movements'

urlpatterns = [
    path('transaction/', RegisterMovement.as_view(), name='transaction')
]