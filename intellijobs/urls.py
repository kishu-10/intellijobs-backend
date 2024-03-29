"""intellijobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views

from intellijobs.token import CustomTokenObtainPairView


urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    # URLs for token authentication
    path('api/token/', CustomTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/',
         jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # URLs for apps
    path('dashboard/', include('dashboard.urls')),
    path('api/jobs/', include('jobs.urls') ),
    path('api/users/', include('users.urls') ),
    path('api/cv-builder/', include('cvbuilder.urls') ),
    path('api/feeds/', include('feeds.urls') ),

]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
