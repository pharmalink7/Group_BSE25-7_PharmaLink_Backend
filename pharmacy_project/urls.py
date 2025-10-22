# pharmacy_project/urls.py

from django.contrib import admin
from django.urls import path, include
from apps.pharmacies.views import index 

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),

     path('', include('django_prometheus.urls')),   # exposes /metrics
    
    # App URLs
    path('api/', include('apps.pharmacies.urls')), 
    path('api/users/', include('apps.users.urls')),

    # JWT Login URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]