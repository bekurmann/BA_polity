"""polity URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# import routers from apps
from legislatives.api.urls import router as legislatives_router
from politicans.api.urls import router as politicans_router

# for media files
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()

# local apps extend DefaultRouter
router.registry.extend(legislatives_router.registry)
router.registry.extend(politicans_router.registry)

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    
    # browsable api; only for dev
    path('api/api-auth/', include('rest_framework.urls')),
    
    # authentication
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),

    # router
    path('api/v1/', include(router.urls))
]

# media files

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# # admin look customization
# # obsolete with django-admin-interface
# admin.site.site_header = "polity Admin"
# admin.site.site_title = "polity Admin Portal"
# admin.site.index_title = "Welcome to polity Portal"