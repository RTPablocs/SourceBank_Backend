from django.urls import path
from .views import *

app_name = 'notifications'

urlpatterns = [
    path('read/', UpdateNotification.as_view(), name='transaction')
]