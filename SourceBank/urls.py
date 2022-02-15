"""SourceBank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import url as user_urls
from movements import urls as movements_urls
from rest_framework import routers
from notifications import urls as nots_urls
from channels.routing import ProtocolTypeRouter
router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('user/', include(user_urls)),
    path('movements/', include(movements_urls)),
    path('notifications/', include(nots_urls)),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework'))
]
