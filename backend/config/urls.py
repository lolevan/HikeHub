"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from apps.hikes.views import HikeListView, HikeDetailView
from apps.applications.views import ApplicationCreateView


urlpatterns = [
    path('admin/', admin.site.urls),

    # Публичные API (без авторизации)
    path('api/v1/public/hikes/', HikeListView.as_view(), name='hike-list'),
    path('api/v1/public/hikes/<int:pk>/', HikeDetailView.as_view(), name='hike-detail'),
    path('api/v1/public/hikes/<int:hike_id>/applications/', ApplicationCreateView.as_view(), name='application-create'),

    # Приватные API (панель управления) — аутентификация JWT
    path('api/v1/private/users/', include('apps.users.urls')),
]
